#!/usr/bin/env python3
"""Download a YouTube video with yt-dlp."""

import argparse
from pathlib import Path

from yt_dlp import YoutubeDL


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Download a YouTube video to a local folder.",
    )
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "--output-dir",
        default="downloads",
        help="Directory to save the downloaded file (default: downloads)",
    )
    parser.add_argument(
        "--format",
        default="best",
        help="yt-dlp format selector (default: best)",
    )
    parser.add_argument(
        "--filename",
        default="%(title)s.%(ext)s",
        help="Output filename template (default: %(title)s.%(ext)s)",
    )
    return parser


def download_video(url: str, output_dir: Path, filename_template: str, fmt: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    ydl_opts = {
        "outtmpl": str(output_dir / filename_template),
        "format": fmt,
        "noplaylist": True,
        "restrictfilenames": True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    download_video(
        url=args.url,
        output_dir=Path(args.output_dir),
        filename_template=args.filename,
        fmt=args.format,
    )


if __name__ == "__main__":
    main()
