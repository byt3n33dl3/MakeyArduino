from pynput.keyboard import Listener, KeyCode
import cv2

TRIGGER_KEY = KeyCode(char='a')

def play_video(video_path):

    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return
    
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Video', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'): #Q to quit video display
                break
        else:
            break
    
    cap.release()
    cv2.destroyAllWindows()

def on_press(key):

    if key == TRIGGER_KEY:
        print("Trigger key pressed. Playing video")
        play_video(video_path)

with Listener(on_press=on_press) as listener:
    listener.join()

    TRIGGER_KEY = KeyCode(char='d')

def play_video(video_path):

    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return
    
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Video', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'): #Q to quit video display
                break
        else:
            break
    
    cap.release()
    cv2.destroyAllWindows()

def on_press(key):

    if key == TRIGGER_KEY:
        print("Trigger key pressed. Playing video")
        play_video(video_path)

with Listener(on_press=on_press) as listener:
    listener.join()
