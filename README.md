# PingPongOS

PingPongOS is an open-source AI project for building a table tennis training assistant. The long-term goal is to help players organize practice videos, detect rallies, and generate useful AI coaching feedback.

## Current Development Stage

Sprint 9: Clip Manager

This sprint adds clip management for generated clips. PingPongOS can now scan `output/clips`, print clip metadata, and save a CSV index. AI analysis is not implemented yet.

## Sprint 1: Video Loader

Place table tennis videos in the `input_videos` folder. The scanner currently supports:

- `.mp4`
- `.mov`
- `.avi`
- `.mkv`

Run the scanner from the project root:

```bash
python scripts/scan_videos.py
```

On Windows, if `python` opens the Microsoft Store launcher, use:

```bash
py scripts/scan_videos.py
```

The script prints a readable terminal table with each video's file name, path, duration, FPS, width, and height.

## Sprint 2: Video Player / Frame Reader

Run the player from the project root:

```bash
python scripts/play_video.py
```

The player scans `input_videos`, opens the first supported video, and displays frames in a window named `PingPongOS Player`. Press `q` to quit playback.

## Sprint 4: Video Timeline

The player now displays timeline information directly on the video:

- Current frame index
- Current timestamp
- Total video duration

Playback controls:

- Press `Space` to pause or resume.
- Press `q` to quit.

The timestamp format is `MM:SS.xx`, such as `00:08.37 / 00:18.23`.

## Sprint 5: Frame Snapshot Export

While the player is running, press `s` to save the current displayed frame as a PNG image.

Snapshots are saved to:

```text
output/snapshots/
```

Snapshot files use this naming format:

```text
snapshot_frame_000123.png
```

Playback controls:

- Press `Space` to pause or resume.
- Press `s` to save the current frame.
- Press `q` to quit.

## Sprint 6: Snapshot Index Log

Each time you press `s`, PingPongOS saves the current frame and appends metadata to:

```text
output/snapshots/snapshots.csv
```

The snapshot index includes:

- `snapshot_file`
- `source_video`
- `frame_index`
- `timestamp_seconds`
- `timestamp_label`

The CSV file is created automatically with headers the first time a snapshot is saved.

## Sprint 7: Frame Iterator

PingPongOS now includes a reusable frame iterator that yields:

- `frame`
- `frame_index`
- `timestamp_seconds`

Run the iterator demo from the project root:

```bash
python scripts/iterate_video.py
```

On Windows, if `python` opens the Microsoft Store launcher, use:

```bash
py scripts/iterate_video.py
```

The demo scans `input_videos`, opens the first supported video, prints the first 20 frame timestamps, and exits without displaying an OpenCV window.

## Sprint 8: Video Splitter

PingPongOS now includes a reusable video splitter:

```python
split_video(input_video, output_video, start_seconds, end_seconds)
```

Run the demo from the project root:

```bash
python scripts/split_video.py
```

On Windows, if `python` opens the Microsoft Store launcher, use:

```bash
py scripts/split_video.py
```

The demo scans `input_videos`, opens the first supported video, clips from `2.0` seconds to `5.0` seconds, and saves:

```text
output/clips/demo_clip.mp4
```

## Sprint 9: Clip Manager

PingPongOS now includes a clip manager that scans generated clips and builds an index.

Run the manager from the project root:

```bash
python scripts/manage_clips.py
```

On Windows, if `python` opens the Microsoft Store launcher, use:

```bash
py scripts/manage_clips.py
```

The script scans:

```text
output/clips/
```

It prints a readable table and saves:

```text
output/clips/clips.csv
```

The clip index includes stable fields for future analysis and labeling:

- `clip_name`
- `clip_path`
- `source_video`
- `start_seconds`
- `end_seconds`
- `start_frame`
- `end_frame`
- `label`
- `duration_seconds`
- `fps`
- `width`
- `height`

## Planned Roadmap

- V0.1 Project Initialization
- V0.2 Video Loader
- V0.3 Video Player / Frame Reader
- V0.4 Video Timeline
- V0.5 Frame Snapshot Export
- V0.6 Snapshot Index Log
- V0.7 Frame Iterator
- V0.8 Video Splitter
- V0.9 Clip Manager
- V0.10 Rally Detection
- V0.11 AI Coaching Report
