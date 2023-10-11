
# YouTube Video Summarizer 🎬

**YouTube Video Summarizer** is a Python package that makes keeping up with your favorite YouTube channels a breeze. It fetches recent videos, converts audio to text, summarizes content, and turns it into speech, all with a user-friendly touch. Say goodbye to long video sessions and hello to efficient content discovery!

## Table of Contents
- [Features](#features)
- [What It Does](#what-it-does)
- [Getting Started](#getting-started)
  - [Quick Setup](#quick-setup)
  - [Simple Usage](#simple-usage)
- [Advanced Options](#advanced-options)
- [Contribute](#contribute)
- [License](#license)

## Features
- Get recent videos from a YouTube channel.
- Convert video audio to text with Google's Speech-to-Text API.
- Summarize video content using OpenAI's GPT-3.
- Convert summaries to speech with ElevenLabs' API.
- Save speech summaries as MP3 files for easy listening.

## What It Does
In a world overflowing with information, **YouTube Video Summarizer** steps in to keep things simple and user-friendly:

1. **Fetching Recent Videos**: The package gathers the latest videos from your chosen YouTube channel.

2. **Transcribing Audio**: It turns spoken words in videos into text using Google's Speech-to-Text API.

3. **Summarizing Content**: Harnessing the power of OpenAI's GPT-3, it distills video content into concise summaries, giving you the heart of each video.

4. **Converting to Speech**: The package then transforms these summaries into speech with ElevenLabs' API, creating MP3 files for easy listening.

Now you can swiftly understand the essence of every video, sparing you the effort of watching long content.

## Getting Started
### Quick Setup
To start using **YouTube Video Summarizer**, install the package and configure the required API keys:

```bash
pip install youtube-video-summarizer
```

### Simple Usage
Using the package couldn't be easier:

```python
from youtube_video_summarizer import main_function

# Fetch, transcribe, summarize, and convert to speech the recent videos from a YouTube channel
mp3_files = main_function('your_channel_id')

# mp3_files is a list of paths to the MP3 files containing the speech summaries of the videos
```

## Advanced Options
For those seeking customization, dive into our [documentation](https://github.com/your-repo/docs) to explore advanced options for transcription, summarization, and speech conversion.

## Contribute
Contributions are encouraged! Feel free to open issues, submit pull requests, or enhance our documentation. Check out our [Contribution Guide](CONTRIBUTING.md) for more details.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README maintains simplicity and user-friendliness, aligning with Steve Wozniak's ethos of making technology accessible and easy to use. Replace `'your_channel_id'` with actual channel IDs and link to your documentation or resources as needed.
