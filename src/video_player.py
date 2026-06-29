import cv2


WINDOW_NAME = "PingPongOS Player"
DEFAULT_FPS = 30
FRAME_LABEL_POSITION = (20, 40)


def play_video(video_path: str) -> None:
    """Open a video and display it frame by frame."""
    capture = cv2.VideoCapture(video_path)
    if not capture.isOpened():
        print(f"Error: Could not open video file: {video_path}")
        return

    fps = capture.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = DEFAULT_FPS

    frame_delay = max(1, int(1000 / fps))
    paused = False
    frame_index = 0
    current_frame = None

    try:
        while True:
            if not paused:
                success, frame = capture.read()
                if not success:
                    break

                frame_index += 1
                current_frame = frame.copy()
                cv2.putText(
                    current_frame,
                    f"Frame: {frame_index}",
                    FRAME_LABEL_POSITION,
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA,
                )
                cv2.imshow(WINDOW_NAME, current_frame)
            elif current_frame is not None:
                cv2.imshow(WINDOW_NAME, current_frame)

            key = cv2.waitKey(frame_delay if not paused else 30) & 0xFF
            if key == ord("q"):
                break
            if key == ord(" "):
                paused = not paused
    finally:
        capture.release()
        cv2.destroyAllWindows()
