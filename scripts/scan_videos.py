from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.video_loader import scan_videos


def print_video_table(videos: list[dict]) -> None:
    if not videos:
        print("No supported videos found in input_videos.")
        return

    headers = ["File Name", "Duration (s)", "FPS", "Width", "Height", "Path"]
    rows = [
        [
            video["file_name"],
            f"{video['duration_seconds']:.2f}",
            f"{video['fps']:.2f}",
            str(video["width"]),
            str(video["height"]),
            video["file_path"],
        ]
        for video in videos
    ]

    column_widths = [
        max(len(str(row[index])) for row in [headers, *rows])
        for index in range(len(headers))
    ]

    header_line = " | ".join(
        header.ljust(column_widths[index]) for index, header in enumerate(headers)
    )
    separator = "-+-".join("-" * width for width in column_widths)

    print(header_line)
    print(separator)
    for row in rows:
        print(
            " | ".join(
                value.ljust(column_widths[index]) for index, value in enumerate(row)
            )
        )


def main() -> None:
    videos = scan_videos("input_videos")
    print_video_table(videos)


if __name__ == "__main__":
    main()
