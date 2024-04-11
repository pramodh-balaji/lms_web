# transcript.py
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from urllib.parse import urlparse, parse_qs

API_KEY = 'YOUR_YOUTUBE_API_KEY'

def fetch_transcript(video_url):
    video_id = parse_qs(urlparse(video_url).query)['v'][0]
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    try:
        response = youtube.captions().list(part='snippet', videoId=video_id).execute()
        caption_id = response['items'][0]['id']
        caption = youtube.captions().download(id=caption_id, tfmt='ttml').execute()
        transcript = caption.decode('utf-8')
        # Further processing of transcript if needed
        return transcript
    except HttpError:
        return "Transcript not found or API key error"
