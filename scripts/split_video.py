from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.video_loader import scan_videos
from src.video_splitter import split_video


START_SECONDS = 2.0
END_SECONDS = 5.0
OUTPUT_VIDEO = Path("output") / "clips" / "demo_clip.mp4"


def main() -> None:
    videos = scan_videos("input_videos")
    if not videos:
        print("No supported videos found in input_videos.")
        return

    first_video = videos[0]
    input_video = first_video["file_path"]

    print(f"Input video: {first_video['file_name']}")
    print(f"Source path: {input_video}")
    print(f"Clip range: {START_SECONDS:.2f}s to {END_SECONDS:.2f}s")
    print(f"Output path: {OUTPUT_VIDEO}")

    split_video(
        input_video=input_video,
        output_video=str(OUTPUT_VIDEO),
        start_seconds=START_SECONDS,
        end_seconds=END_SECONDS,
    )

    print("Video clip saved successfully.")


if __name__ == "__main__":
    main()
