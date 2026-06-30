from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.frame_iterator import iterate_video
from src.video_loader import scan_videos


def main() -> None:
    videos = scan_videos("input_videos")
    if not videos:
        print("No supported videos found in input_videos.")
        return

    first_video = videos[0]
    print(f"Iterating video: {first_video['file_name']}")
    print(f"Path: {first_video['file_path']}")

    for frame_data in iterate_video(first_video["file_path"]):
        frame_index = frame_data["frame_index"]
        timestamp_seconds = frame_data["timestamp_seconds"]
        print(f"Frame {frame_index} | {timestamp_seconds:.2f} s")

        if frame_index >= 20:
            break


if __name__ == "__main__":
    main()
