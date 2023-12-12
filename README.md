# YouTube Channel Video URL Scraper

This Python script allows you to scrape video URLs from a YouTube channel using the YouTube Data API. It utilizes the `google-api-python-client` library and can store the video URLs in a text file. Additionally, it provides an option to download the videos using `yt_dlp`.

## Prerequisites

Before using the script, ensure you have the following:

1. **Python installed on your machine.**
2. The required Python libraries installed. You can install them using:

   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client python-dotenv yt-dlpd

# Getting Started

## 1. Set up Google API credentials

- Create a project on the Google Cloud Console.
- Enable the YouTube Data API v3 for your project.
- Create API credentials (API key).

## 2. Create a `.env` file

- Create a file named `.env` in the project directory.
- Add your API key and target channel ID to the `.env` file:

  ```env
  API_KEY=YOUR_API_KEY
  CHANNEL_ID=TARGET_CHANNEL_ID

