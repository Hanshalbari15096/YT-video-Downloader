# YT Downloader

A simple Python script to download YouTube videos in the best available quality using `yt-dlp`.

## Requirements

- Python 3.x
- `yt-dlp`

```bash
pip install yt-dlp
```

## Usage

```bash
python YT_Downloader.py
```

Enter the YouTube URL when prompted. The video downloads to a `Downloads/` folder in the current directory.

## Features

- Downloads best available video + audio quality
- Auto-names files using the video title
- Saves to `Downloads/` folder by default

## Using as a Module

```python
from YT_Downloader import download_video

download_video("https://www.youtube.com/watch?v=example")

# Custom output folder
download_video("https://www.youtube.com/watch?v=example", output_folder="MyVideos")
```

## Output

Files are saved as:
```
Downloads/<video_title>.<ext>
```

## Notes

- Requires `ffmpeg` installed on your system for merging video and audio streams.
- Works with any URL supported by `yt-dlp` (not just YouTube).
