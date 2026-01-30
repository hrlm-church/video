# YouTube Video Downloader

A simple Python CLI app for downloading YouTube videos using `yt-dlp`.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python app/download.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Options

- `--output-dir` (default: `downloads`)
- `--format` (default: `best`)
- `--filename` (default: `%(title)s.%(ext)s`)

Example with custom output:

```bash
python app/download.py "https://www.youtube.com/watch?v=VIDEO_ID" \
  --output-dir videos \
  --format "bestvideo+bestaudio/best" \
  --filename "%(title)s.%(ext)s"
```

## Notes

- This tool downloads single videos (no playlists).
- Downloaded files are saved with filesystem-safe names.
