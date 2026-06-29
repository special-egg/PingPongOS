# PingPongOS

PingPongOS is an open-source AI project for building a table tennis training assistant. The long-term goal is to help players organize practice videos, detect rallies, and generate useful AI coaching feedback.

## Current Development Stage

Sprint 1: Video Loader

This sprint adds the first real feature: scanning supported videos in `input_videos` and printing basic metadata. Video splitting and AI analysis are not implemented yet.

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

## Planned Roadmap

- V0.1 Project Initialization
- V0.2 Video Loader
- V0.3 Video Splitter
- V0.4 Rally Detection
- V0.5 AI Coaching Report
