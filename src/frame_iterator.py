import cv2


DEFAULT_FPS = 30


def iterate_video(video_path: str):
    """Yield frames from a video with frame index and timestamp metadata."""
    capture = cv2.VideoCapture(video_path)
    if not capture.isOpened():
        print(f"Error: Could not open video file: {video_path}")
        return

    fps = capture.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = DEFAULT_FPS

    frame_index = 0

    try:
        while True:
            success, frame = capture.read()
            if not success:
                break

            frame_index += 1
            yield {
                "frame": frame,
                "frame_index": frame_index,
                "timestamp_seconds": frame_index / fps,
            }
    finally:
        capture.release()
