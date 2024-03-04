import cv2

def play_video(video_path):
    """
    Play a video file with the given path.
    """
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Video Playback', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    """
    Main function to handle the trigger condition.
    """
    trigger = input("Enter 'play' to play the video: ")
    if trigger.lower() == 'play':
        video_path = '"C:\Users\Sulaiman\Documents\CODE\makey_makey_project\trigger1.mp4"'
        play_video(video_path)
    else:
        print("Trigger condition not met.")

if __name__ == "__main__":
    main()