from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.clip_manager import save_clips_index, scan_clips


CLIPS_DIR = Path("output") / "clips"
CLIPS_INDEX = CLIPS_DIR / "clips.csv"


def print_clips_table(clips: list[dict]) -> None:
    if not clips:
        print("No generated clips found in output/clips.")
        return

    headers = ["Clip Name", "Duration (s)", "FPS", "Width", "Height", "Path"]
    rows = [
        [
            clip["clip_name"],
            f"{clip['duration_seconds']:.2f}",
            f"{clip['fps']:.2f}",
            str(clip["width"]),
            str(clip["height"]),
            clip["clip_path"],
        ]
        for clip in clips
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
    clips = scan_clips(str(CLIPS_DIR))
    print_clips_table(clips)
    save_clips_index(clips, str(CLIPS_INDEX))
    print(f"Saved clip index: {CLIPS_INDEX}")


if __name__ == "__main__":
    main()
