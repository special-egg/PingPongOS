from pathlib import Path

import cv2


MP4_CODEC = "mp4v"


def split_video(
    input_video: str,
    output_video: str,
    start_seconds: float,
    end_seconds: float,
) -> None:
    """Save a video clip from start_seconds to end_seconds as an MP4 file."""
    if start_seconds < 0:
        raise ValueError("start_seconds must be greater than or equal to 0.")
    if end_seconds <= start_seconds:
        raise ValueError("end_seconds must be greater than start_seconds.")

    capture = cv2.VideoCapture(input_video)
    if not capture.isOpened():
        raise ValueError(f"Could not open video file: {input_video}")

    try:
        fps = capture.get(cv2.CAP_PROP_FPS)
        if fps <= 0:
            raise ValueError("Could not read a valid FPS from the video.")

        frame_count = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        duration_seconds = frame_count / fps

        if start_seconds >= duration_seconds:
            raise ValueError("start_seconds must be before the end of the video.")
        if end_seconds > duration_seconds:
            raise ValueError("end_seconds must not exceed the video duration.")
        if width <= 0 or height <= 0:
            raise ValueError("Could not read a valid video resolution.")

        start_frame = int(start_seconds * fps)
        end_frame = int(end_seconds * fps)

        output_path = Path(output_video)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        writer = cv2.VideoWriter(
            str(output_path),
            cv2.VideoWriter_fourcc(*MP4_CODEC),
            fps,
            (width, height),
        )
        if not writer.isOpened():
            raise ValueError(f"Could not create output video: {output_video}")

        try:
            capture.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
            current_frame = start_frame

            while current_frame < end_frame:
                success, frame = capture.read()
                if not success:
                    break

                writer.write(frame)
                current_frame += 1
        finally:
            writer.release()
    finally:
        capture.release()
