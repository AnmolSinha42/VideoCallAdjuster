#include <Arduino_RouterBridge.h>  
#include <AccelStepper.h>

const int step_pin_1 = 5;
const int dir_pin_1 = 6;
const int step_pin_2 = 7;
const int dir_pin_2 = 8;

AccelStepper motor1(AccelStepper::DRIVER, step_pin_1, dir_pin_1);
AccelStepper motor2(AccelStepper::DRIVER, step_pin_2, dir_pin_2);

void pan_camera(int steps) {
  motor1.move(steps*(-1));
}

void tilt_camera(int steps) {
  motor2.move(steps*(-1));
}

void setup() {
  Bridge.begin();
  Bridge.provide("pan_camera", pan_camera);
  Bridge.provide("tilt_camera", tilt_camera);
  
  motor1.setMaxSpeed(400.0);
  motor1.setAcceleration(200.0);
  
  motor2.setMaxSpeed(400.0);
  motor2.setAcceleration(200.0);
}

void loop() {
  Bridge.update();
  motor1.run();
  motor2.run();
}