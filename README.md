# YouTube Channel Video URL Scraper

This Python script allows you to scrape video URLs from a YouTube channel using the YouTube Data API and download them all using yt-dlp.

## Prerequisites

Before using the script, ensure you have the following:

### Python Installed

If you haven't already, visit [here](https://www.python.org/) to install Python for your OS.

### Python Libraries Installed

You can install them using:

`pip install -r requirements.txt`

### yt-dlp Installed

`sudo apt install yt-dlp`

Replace with your OS' package manager.

# Getting Started

## 1. Clone the repo
`git clone https://github.com/Kouei-Lin/yt_dlp_bulk`

`cd yt_dlp_bulk`

## 2. Set up Google API credentials

- Create a project on the [Google Cloud Console](https://console.cloud.google.com/).
- Enable the YouTube Data API v3 for your project.
- Create API credentials (API key).

## 3. Set `.env`
`cp .env_example .env`

Paste in the Youtube API and the channel you want to scrap into `.env`.

Visit [here](https://www.streamweasels.com/tools/youtube-channel-id-and-user-id-convertor/) to convert channel handle to channelID.

## 4. Scrap URLs
`python3 main.py`

It will create a `yt_url.txt` file in the current directory

## 5. Download videos
`chmod +x yt_download.sh`

`./yt_download.sh`

## 6. Enjoy
Videos should be in the `video` folder in the same directory.
