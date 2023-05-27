# 🎬 YouTube Video Summarizer 📝

This Python package fetches recent videos from a specific YouTube channel, transcribes the videos using Google's Speech-to-Text API, summarizes the transcription using OpenAI's GPT-3, and converts the summary to speech using ElevenLabs' API. The summaries are saved as MP3 files.

## 📜 Abstract

In the age of information, staying up-to-date with the latest videos from your favorite YouTube channels can be time-consuming. This package automates the process by fetching recent videos, transcribing the audio, summarizing the content, and converting the summary to speech. This allows you to quickly get the gist of each video without having to watch the entire thing.

## 🚀 Usage

```python
from youtube_video_summarizer import main_function

# Fetch, transcribe, summarize, and convert to speech the recent videos from a YouTube channel
mp3_files = main_function('your_channel_id')

# mp3_files is a list of paths to the MP3 files containing the speech summaries of the videos
