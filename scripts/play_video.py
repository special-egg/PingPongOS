from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.video_loader import scan_videos
from src.video_player import play_video


def main() -> None:
    videos = scan_videos("input_videos")
    if not videos:
        print("No supported videos found in input_videos.")
        return

    first_video = videos[0]
    print(f"Playing video: {first_video['file_name']}")
    print(f"Path: {first_video['file_path']}")
    play_video(first_video["file_path"])


if __name__ == "__main__":
    main()
