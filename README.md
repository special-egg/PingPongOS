# PingPongOS

PingPongOS is an open-source AI project for building a table tennis training assistant. The long-term goal is to help players organize practice videos, detect rallies, and generate useful AI coaching feedback.

## Current Development Stage

Sprint 4: Video Timeline

This sprint adds a timeline layer to OpenCV playback. The player now shows frame position and timestamps while preserving FPS-based playback, pause, and quit controls. Video splitting and AI analysis are not implemented yet.

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

## Planned Roadmap

- V0.1 Project Initialization
- V0.2 Video Loader
- V0.3 Video Player / Frame Reader
- V0.4 Video Timeline
- V0.5 Video Splitter
- V0.6 Rally Detection
- V0.7 AI Coaching Report
