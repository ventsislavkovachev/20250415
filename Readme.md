# Anti-Scam AI Project

## Project Overview

This project aims to develop an AI-powered tool to waste the time of phone scammers by engaging them in convincing conversations. The AI simulates a victim persona and interacts with scammers using speech recognition, a large language model (LLM), and text-to-speech (TTS) technologies. The goal is to keep scammers occupied for as long as possible, reducing their ability to target real victims.

## Features

### Core Functionality
1. **Speech Recognition**: 
   - Uses Google Cloud Speech-to-Text API to transcribe audio input from scammers.
   - Handles cases where no voice is detected by recursively prompting for input.

2. **AI-Driven Responses**:
   - Employs the Nebius LLM API to generate contextually appropriate responses.
   - The AI is initialized with a detailed system prompt that defines the context, scam description, victim persona, and behavioral instructions.

3. **Text-to-Speech (TTS)**:
   - Converts AI-generated text responses into speech using Google Cloud Text-to-Speech API.
   - Outputs audio in a female voice with a friendly and engaging tone.

4. **Audio Playback**:
   - Plays the generated audio responses to the scammer using the Pygame mixer library.

### Advanced Features
1. **Sentiment Analysis**:
   - Analyzes the scammer's tone and sentiment using libraries like VaderSentiment, TextBlob, and pre-trained NLP models.
   - Adjusts the AI's behavior dynamically based on sentiment scores.

2. **Emotion and Intent Detection**:
   - Detects emotions, urgency, and intent in the scammer's speech using NLP techniques and pre-trained models.
   - Extracts key aspects and contextual subtleties to refine responses.

3. **Natural Conversation Enhancements**:
   - Introduces hesitations, pauses, and lapses in speech to make the AI more human-like.
   - Varies response lengths and reformulates sentences for clarity.

4. **Scam-Specific Context**:
   - The AI is programmed to simulate a 25-year-old Parisian woman named Louise Bernard, who is naive, overly trusting, and eager to engage with the scammer.

## Installation Instructions

1. **Set Up Virtual Environment**:
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1

2. **Install Dependencies**:
   pip install huggingface_hub google-cloud-texttospeech google-cloud-speech sounddevice soundfile pygame vaderSentiment spacy textblob transformers nltk

3. **Download Language Models**:
   - For spaCy:
     python -m spacy download fr_core_news_lg

   - For NLTK:
     python -m nltk.downloader punkt

4. **Set Up API Keys**:
   - Place your Nebius API key in nebius_api_key.txt.
   - Place your Google Cloud credentials in google_key.json.

5. **Run the Program**:
   python anti-scam.py

## Usage Instructions

1. Start the program and allow it to record audio from the scammer.
2. The AI will transcribe the scammer's speech, analyze it, and generate a response.
3. The response will be converted to speech and played back to the scammer.
4. The process continues until the scammer says "stop."

## Technical Details

### Code Structure
- **Speech Recognition**: `escroc_speech_to_text()`
- **AI Response Generation**: `victim_get_AI_input()`
- **Text-to-Speech Conversion**: `victim_AI_text_to_speach()`
- **Sentiment Analysis**: `analyser_les_sentiments()`
- **Audio Playback**: `victim_play_audio_file()`

### Libraries and APIs
- **Google Cloud APIs**: Speech-to-Text and Text-to-Speech.
- **Nebius LLM API**: For generating conversational responses.
- **NLP Libraries**: spaCy, TextBlob, VaderSentiment, and Transformers.
- **Audio Processing**: SoundDevice, SoundFile, and Pygame.

## Future Enhancements

1. **Emotion Recognition**:
   - Improve detection of emotions and tone in scammer speech.
   - Adjust AI responses to reflect detected emotions.

2. **Dynamic Voice Modulation**:
   - Add support for varying voice tones and speeds based on context.

3. **Silence Detection**:
   - Detect and handle long pauses in the scammer's speech.

4. **Multi-Language Support**:
   - Extend support to other languages for broader applicability.

5. **Behavioral Analytics**:
   - Log and analyze scammer behavior to refine AI strategies.

## Authors
- Ventsislav Kovachev

## License
This project is licensed under [Your Chosen License].

## Acknowledgments
- Hugging Face for the LLM API.
- Google Cloud for Speech-to-Text and Text-to-Speech services.
- Open-source NLP libraries like spaCy, TextBlob, and Transformers.