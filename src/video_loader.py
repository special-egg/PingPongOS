from pathlib import Path

import cv2


SUPPORTED_VIDEO_EXTENSIONS = {".mp4", ".mov", ".avi", ".mkv"}


def scan_videos(input_dir: str) -> list[dict]:
    """Scan a directory for supported videos and return basic metadata."""
    video_dir = Path(input_dir)
    if not video_dir.exists() or not video_dir.is_dir():
        return []

    videos = []
    for video_path in sorted(video_dir.iterdir()):
        if not video_path.is_file():
            continue

        if video_path.suffix.lower() not in SUPPORTED_VIDEO_EXTENSIONS:
            continue

        capture = cv2.VideoCapture(str(video_path))
        if not capture.isOpened():
            continue

        fps = capture.get(cv2.CAP_PROP_FPS)
        frame_count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        duration_seconds = frame_count / fps if fps > 0 else 0
        capture.release()

        videos.append(
            {
                "file_name": video_path.name,
                "file_path": str(video_path),
                "duration_seconds": duration_seconds,
                "fps": fps,
                "width": width,
                "height": height,
            }
        )

    return videos
