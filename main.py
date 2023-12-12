import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load environment variables from .env
load_dotenv()

# Get API key and channel ID from environment variables
API_KEY = os.getenv('API_KEY')
CHANNEL_ID = os.getenv('CHANNEL_ID')

def get_video_urls(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    playlist_response = youtube.channels().list(part='contentDetails', id=channel_id).execute()
    playlist_id = playlist_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    while True:
        playlist_items = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        videos.extend(item['contentDetails']['videoId'] for item in playlist_items['items'])

        next_page_token = playlist_items.get('nextPageToken')
        if not next_page_token:
            break

    video_urls = [f'https://www.youtube.com/watch?v={video_id}' for video_id in videos]
    return video_urls

def write_to_txt(file_path, video_urls):
    with open(file_path, 'w') as file:
        for url in video_urls:
            file.write(url + '\n')

if __name__ == "__main__":
    video_urls = get_video_urls(API_KEY, CHANNEL_ID)
    
    # Define the file path where you want to store the URLs
    txt_file_path = 'yt_url.txt'
    
    # Write URLs to the text file
    write_to_txt(txt_file_path, video_urls)
    
    print(f'Video URLs are stored in {txt_file_path}')

