import csv
from pathlib import Path

import cv2


SUPPORTED_CLIP_EXTENSIONS = {".mp4", ".mov", ".avi", ".mkv"}
CLIP_INDEX_HEADERS = [
    "clip_name",
    "clip_path",
    "source_video",
    "start_seconds",
    "end_seconds",
    "start_frame",
    "end_frame",
    "label",
    "duration_seconds",
    "fps",
    "width",
    "height",
]


def scan_clips(clips_dir: str) -> list[dict]:
    """Scan generated clips and return basic metadata."""
    clip_dir = Path(clips_dir)
    if not clip_dir.exists() or not clip_dir.is_dir():
        return []

    clips = []
    for clip_path in sorted(clip_dir.iterdir()):
        if not clip_path.is_file():
            continue

        if clip_path.suffix.lower() not in SUPPORTED_CLIP_EXTENSIONS:
            continue

        capture = cv2.VideoCapture(str(clip_path))
        if not capture.isOpened():
            continue

        fps = capture.get(cv2.CAP_PROP_FPS)
        frame_count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
        width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        duration_seconds = frame_count / fps if fps > 0 else 0
        capture.release()

        clips.append(
            {
                "clip_name": clip_path.name,
                "clip_path": str(clip_path),
                "source_video": "",
                "start_seconds": 0,
                "end_seconds": 0,
                "start_frame": 0,
                "end_frame": 0,
                "label": "",
                "duration_seconds": duration_seconds,
                "fps": fps,
                "width": width,
                "height": height,
            }
        )

    return clips


def save_clips_index(clips: list[dict], output_csv: str) -> None:
    """Save clip metadata to a CSV file."""
    output_path = Path(output_csv)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CLIP_INDEX_HEADERS)
        writer.writeheader()

        for clip in clips:
            writer.writerow(
                {
                    "clip_name": clip["clip_name"],
                    "clip_path": clip["clip_path"],
                    "source_video": clip["source_video"],
                    "start_seconds": clip["start_seconds"],
                    "end_seconds": clip["end_seconds"],
                    "start_frame": clip["start_frame"],
                    "end_frame": clip["end_frame"],
                    "label": clip["label"],
                    "duration_seconds": f"{clip['duration_seconds']:.2f}",
                    "fps": f"{clip['fps']:.2f}",
                    "width": clip["width"],
                    "height": clip["height"],
                }
            )
