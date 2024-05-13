from youtube_transcript_api import YouTubeTranscriptApi  
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound  
import re  
  
def extract_video_id(youtube_url: str) -> str:  
    """  
    Extracts the video ID from a YouTube URL.  
  
    Args:  
        youtube_url (str): The YouTube URL.  
  
    Returns:  
        str: The extracted video ID.  
    """  
    video_id_match = re.search(r'v=([0-9A-Za-z_-]{11})', youtube_url)  
    if video_id_match:  
        return video_id_match.group(1)  
    raise ValueError('Invalid YouTube URL')  
  
def get_youtube_transcript(youtube_url: str) -> str:  
    """  
    Fetches the transcript for a YouTube video without needing an API key.  
  
    Args:  
        youtube_url (str): The full URL of the YouTube video.  
  
    Returns:  
        str: The transcript of the video as a string.  
    """  
    try:  
        video_id = extract_video_id(youtube_url)  
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)  
        # Concatenating all text elements in the transcript list  
        transcript = '\n'.join([entry['text'] for entry in transcript_list])  
        return transcript  
    except TranscriptsDisabled:  
        return "Transcripts are disabled for this video."  
    except NoTranscriptFound:  
        return "No transcript found for this video."  
    except ValueError as e:  
        return str(e)  
  
# Replace the following URL with the YouTube video URL you want to fetch the transcript for  
youtube_url = 'https://www.youtube.com/watch?v=YOUR_VIDEO_ID'  
transcript = get_youtube_transcript(youtube_url)  
  
print('Transcript:\n', transcript)  
