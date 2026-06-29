from pathlib import Path

import cv2


WINDOW_NAME = "PingPongOS Player"
DEFAULT_FPS = 30
SNAPSHOT_DIR = Path("output") / "snapshots"
TEXT_COLOR = (0, 255, 0)
TEXT_SCALE = 1
TEXT_THICKNESS = 2
FRAME_LABEL_POSITION = (20, 40)
TIME_LABEL_POSITION = (20, 80)


def format_timestamp(seconds: float) -> str:
    """Format seconds as MM:SS.xx."""
    minutes = int(seconds // 60)
    remaining_seconds = seconds % 60
    return f"{minutes:02d}:{remaining_seconds:05.2f}"


def draw_timeline(
    frame,
    frame_index: int,
    fps: float,
    total_duration_seconds: float,
):
    current_timestamp = frame_index / fps
    cv2.putText(
        frame,
        f"Frame: {frame_index}",
        FRAME_LABEL_POSITION,
        cv2.FONT_HERSHEY_SIMPLEX,
        TEXT_SCALE,
        TEXT_COLOR,
        TEXT_THICKNESS,
        cv2.LINE_AA,
    )
    cv2.putText(
        frame,
        (
            f"Time: {format_timestamp(current_timestamp)} / "
            f"{format_timestamp(total_duration_seconds)}"
        ),
        TIME_LABEL_POSITION,
        cv2.FONT_HERSHEY_SIMPLEX,
        TEXT_SCALE,
        TEXT_COLOR,
        TEXT_THICKNESS,
        cv2.LINE_AA,
    )
    return frame


def save_snapshot(frame, frame_index: int) -> None:
    """Save the current displayed frame as a PNG snapshot."""
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    snapshot_path = SNAPSHOT_DIR / f"snapshot_frame_{frame_index:06d}.png"
    cv2.imwrite(str(snapshot_path), frame)
    print(f"Saved snapshot: {snapshot_path}")


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
    frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    total_duration_seconds = frame_count / fps if fps > 0 else 0
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
                current_frame = draw_timeline(
                    current_frame,
                    frame_index,
                    fps,
                    total_duration_seconds,
                )
                cv2.imshow(WINDOW_NAME, current_frame)
            elif current_frame is not None:
                cv2.imshow(WINDOW_NAME, current_frame)

            key = cv2.waitKey(frame_delay if not paused else 30) & 0xFF
            if key == ord("q"):
                break
            if key == ord(" "):
                paused = not paused
            if key == ord("s") and current_frame is not None:
                save_snapshot(current_frame, frame_index)
    finally:
        capture.release()
        cv2.destroyAllWindows()
