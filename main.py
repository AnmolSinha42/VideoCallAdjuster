from arduino.app_utils import App, Bridge
from arduino.app_bricks.video_objectdetection import VideoObjectDetection

video_detector = VideoObjectDetection(confidence=0.4, debounce_sec=0.1) # Kept debounce low

def on_all_detections(detections: dict):
    if not detections or 'face' not in detections or len(detections['face']) == 0:
        return 

    coordinates_xyxy = detections['face'][0]['bounding_box_xyxy']
    center_x, center_y = 319, 239

    face_x = (coordinates_xyxy[0] + coordinates_xyxy[2]) // 2
    face_y = (coordinates_xyxy[1] + coordinates_xyxy[3]) // 2
    
    correction_x = center_x - face_x
    correction_y = center_y - face_y 
    
    deadzone = 30 

    if abs(correction_x) > deadzone:
        steps_to_move_x = int(correction_x * 0.01) 
        Bridge.call("pan_camera", steps_to_move_x) #motor1
        
    if abs(correction_y) > deadzone:
        steps_to_move_y = int(correction_y * 0.01) 
        Bridge.call("tilt_camera", steps_to_move_y) #motor2

video_detector.on_detect_all(on_all_detections)
App.run()