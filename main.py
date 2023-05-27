import os
import requests
from google.cloud import speech_v1p1beta1 as speech
import openai
from pydub import AudioSegment

# Set your API keys
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path_to_your_google_credentials.json"
openai.api_key = 'your_openai_key'

def main_function(channel_id):
    """
    This function fetches recent videos from a specific YouTube channel, transcribes the videos using Google's Speech-to-Text API, summarizes the transcription using OpenAI's GPT-3, and converts the summary to speech using ElevenLabs' API.

    Args:
    channel_id (str): The ID of the YouTube channel to fetch videos from.

    Returns:
    list: A list of paths to the MP3 files containing the speech summaries of the videos.
    """

    # YouTube Data API parameters
    api_key = 'your_youtube_api_key'

    # Fetch recent videos from the YouTube channel
    response = requests.get(
        f'https://www.googleapis.com/youtube/v3/search?order=date&part=snippet&channelId={channel_id}&maxResults=5&key={api_key}'
    )
    video_ids = [item['id']['videoId'] for item in response.json()['items']]

    mp3_files = []

    for video_id in video_ids:
        # Download the video using youtube_dl
        os.system(f'youtube-dl -x --audio-format "wav" -o "{video_id}.%(ext)s" https://www.youtube.com/watch?v={video_id}')

        # Transcribe the audio using Google's Speech-to-Text API
        client = speech.SpeechClient()
        with open(f'{video_id}.wav', 'rb') as audio_file:
            audio = speech.RecognitionAudio(content=audio_file.read())
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )
        response = client.recognize(config=config, audio=audio)
        transcription = ' '.join([result.alternatives[0].transcript for result in response.results])

        # Summarize the transcription using OpenAI's GPT-3
        prompt = f"I have a transcript of a video and I need a summary. Here's the transcript:\n\n{transcription}\n\nSummary:"
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
        summary = response.choices[0].text.strip()

        # Convert the summary to speech using ElevenLabs' API
        response = requests.post(
            'https://api.elevenlabs.ai/synthesize',
            headers={'Authorization': 'Bearer your_elevenlabs_api_key'},
            json={'text': summary, 'voice': 'en-US-Wavenet-D'}
        )
        with open(f'{video_id}_summary.wav', 'wb') as audio_file:
            audio_file.write(response.content)

        # Convert the WAV file to MP3
        sound = AudioSegment.from_wav(f'{video_id}_summary.wav')
        sound.export(f'{video_id}_summary.mp3', format="mp3")

        mp3_files.append(f'{video_id}_summary.mp3')

    return mp3_files
