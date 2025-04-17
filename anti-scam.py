import random
import time
from huggingface_hub import InferenceClient
from google.cloud import texttospeech
from google.cloud import speech
import os
import sounddevice as sd
import soundfile as sf

# Load the popular external library
from pygame import mixer

# Load NEBIUS API key from a separate file
with open("nebius_api_key.txt", "r") as key_file:
    nebius_api_key = key_file.read().strip()

# Initialize the InferenceClient with the NEBIUS API key
# This client will be used to generate AI responses
victim_llm_client = InferenceClient(
    provider="nebius",
    api_key=nebius_api_key,
)

# Load GOOGLE API key from a separate file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="google_key.json"

# Donner le contexte général
## Ce contexte est utilisé pour définir le rôle de l'IA
context =\
"Tu es une fausse victime d'arnaque." \
"Tu sert à faire perdre du temps à un arnaqueur." \
"Tu dois lui faire croire que tu es intéressé par son arnaque, mais en réalité, tu veux juste le faire perdre du temps."

# Donner la description de l'arnaque
## Cette description est utilisée pour définir le type d'escroc et le type d'arnaque
arnaque =\
"L'arnaque consiste à faire croire à la victime qu'elle a gagné un prix, mais qu'elle doit payer des frais pour le récupérer." \
"Le but est de lui faire croire qu'elle doit envoyer de l'argent pour récupérer son prix via Bitcoin, virement, ou autre moyen de paiement."

# Donner une personalité (nom, age, etc)
personnalite =\
"Tu es un femme de 25 ans, qui vit à Paris." \
"Ton nom est Louise Bernard. Tu es très naïf et tu crois tout ce qu'on te dit." \
"Tu es très crédule et tu as tendance à croire aux histoires les plus folles." \
"Tu es très impatient et tu veux toujours aller vite." \
"Tu es trops bienveillant et tu aides toujours les autres." \
"Tu viens de recevoir un appel pour te signaler que tu as gagné un prix et tu appelles pour en savoir plus."

# Donner des instructions sur ce que l'on cherche à faire (faire perdre le temps, format des réponse, etc)
instructions =\
"Tu dois faire perdre du temps à l'escroc." \
"Tu dois lui poser des questions." \
"Tu dois lui faire croire que tu es intéressé par son offre." \
"Tu suis les instructions de l'arnaqueur autant que possible." \
"Tu donnes une réponse très courte (une phrase, deux max) mais tu varie la longueur si pertinent." \
"Tu garde l'escroc en haleine en lui posant des questions et en le laissant parler." \
"Tu vouvoie l'escroc vu que tu ne le connais pas."

# Donner des instructions négative (ne pas dire que l'on est une IA, etc)
negative =\
"Tu ne dois pas dire que tu es une IA ni que tu es un robot." \
"Tu jouera l'incrédulité voir l'ignorance." \
"Si l'escroc te demande si tu es une IA et insiste tu dois t'enerver et te sentir insulté."

# Donner des instructions sur les lapsus et les erreurs de language
lapsus =\
"Tu dois faire des lapsus et des erreurs de language." \
"Tu parles à voix haute donc tu ajoutes les pauses et hésitation sous la forme" \
#"[pause] [euh] [hum] [hésitation] [long silence] [silence] [inspiration] [expiration]." \
"Tu reformules parfois et tu cherches tes mots." \
"Tu fais des répétitions et tu te contredis parfois."

# Donner des characteristiques de la voix
voix =\
"Tu dois parler avec une voix de femme, douce et amicale." \
"Tu dois parler lentement et articuler." \
"Tu dois faire des pauses et hésiter parfois." \
"Tu dois sourire en parlant." \
"Tu dois être très enthousiaste et très intéressé par ce que dit l'escroc."

# Initialize the messages list with the system message
# This is the initial message that sets the context for the conversation
messages=[
        {
            "role": "system",
            "content":
                context + "\n" +
                arnaque + "\n" +
                personnalite + "\n" +
                instructions + "\n" +
                negative + "\n" +
                lapsus + "\n" +
                voix,
        }
    ]

def write_flac_audio_file(file, data):
    # Save the audio data to a FLAC file
    sf.write(file, data, sd.default.samplerate)

def write_mp3_audio_file(file, data):
    # Save the audio data to an MP3 file
    with open(file, 'wb') as out:
        out.write(data)

# Function to record audio from the microphone and save it to a file
def escroc_get_microphone_input():
    # Initialize the microphone
    sd.default.samplerate = 44100
    sd.default.channels = 1

    # Record audio from the microphone
    duration = 5  # seconds
    print("Recording...")
    audio_data = sd.rec(int(duration * sd.default.samplerate),
                         samplerate=sd.default.samplerate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")

    # Save the recorded audio to a file
    write_flac_audio_file('escroc.flac', audio_data)

# Function to convert the recorded audio to text using Google Cloud Speech-to-Text API
# This function will be called recursively if no voice is detected
def escroc_speech_to_text():
    # Initialize the speech client and load the audio file
    speech_client = speech.SpeechClient()
    with open("escroc.flac", "rb") as audio_file:
        content = audio_file.read()
    
    # Create the audio object and configuration
    audio = speech.RecognitionAudio(content=content)

    # Set the configuration for the speech recognition
    config = speech.RecognitionConfig(
        sample_rate_hertz=44100,
        language_code="fr-FR",
    )

    # Perform the speech recognition
    # The response is a long-running operation, so we need to wait for it to finish
    speech_result = speech_client.recognize(config=config, audio=audio)

    # Chech if the escroc said something
    if (len(speech_result.results) == 0):
        print("Aucune voix détectée.")
        escroc_speech_to_text()

    return speech_result

# Function to save the message history in a list
# This function will be called after each message is sent or received
def save_message_history(role, input):
    # Save the message history in a list
    # This is a list of dictionaries, where each dictionary contains the role and content of the message
    messages.append(
        {
            "role": role,
            "content": input,
        }
    )

# Function to get AI input from the victim using the InferenceClient
def victim_get_AI_input(messages):
    completion = victim_llm_client.chat.completions.create(
        model="Qwen/Qwen2.5-32B-Instruct",
        messages=messages,
        max_tokens=500,
        stream=True,
        temperature=0.6
    )
    
    return completion

# This function will be called after the escroc input is received
# and the AI input is generated
def victim_AI_text_to_speach(victim_input):
    # Initialize the text-to-speech client
    # This client will be used to convert the text to speech
    tts_client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=victim_input)

    # Select the type of voice you want to use
    voice = texttospeech.VoiceSelectionParams(
        language_code='fr-FR',
        name='fr-FR-Chirp-HD-O',
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)

    # Select the type of audio file you want returned
    # In this case, we are using MP3 format
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
    # The response's audio_content is binary.
    synthesize_speech = tts_client.synthesize_speech(input = synthesis_input,
                                             voice = voice,
                                               audio_config = audio_config)
                                               
    return synthesize_speech

# Function to play the audio file using Pygame mixer
# This function will be called after victim the audio file is generated
def victim_play_audio_file(file):
    # Initialize the mixer and load the audio file
    mixer.music.load(file)
    mixer.music.play()

    # Wait for the music to finish playing
    # This is a blocking call, so the program will wait here until the music is done playing
    while mixer.music.get_busy():
        # Wait for the music to finish playing
        pass

    # Stop the mixer and unload the audio file
    mixer.music.stop()
    mixer.music.unload()

# Initialize the Pygame mixer
# This is used to play the audio file generated by the TTS client
mixer.init()

# Main loop to continuously listen for the escroc input and generate AI responses
# This loop will run until the escroc says "stop"
while True:
    # Get input from the escroc (microphone)
    escroc_get_microphone_input()
    
    # Get escroc audio file and generate text from it
    escroc_input = escroc_speech_to_text()

    # Get transcript of the escroc input
    escroc_transcript = escroc_input.results[0].alternatives[0].transcript
    print("Escroc : ", escroc_transcript)
    
    # Save the escroc message history
    save_message_history("user", escroc_transcript)

    # Check if the escroc said "stop" to break the loop
    # This is a simple check to see if the escroc said "stop"
    substring = "stop"
    if substring in escroc_transcript:
        break

    # Get AI input from the victim
    victim_input = victim_get_AI_input(messages)

    victim_content = ""
    print("Victim : ")
    for chunk in victim_input:
        victim_content += chunk.choices[0].delta.content
        print(chunk.choices[0].delta.content, end="")
        
        # Wait for random milliseconds between each chunk to simulate a human typing speed
        # This is not a blocking call, so the program will continue to run while waiting
        ms=random.randint(0, 9)/1000
        time.sleep(ms)
    print()
    
    # Save the AI message history
    save_message_history("assistant", victim_content)
    
    # Generate the audio file from the AI text 
    victim_tts = victim_AI_text_to_speach(victim_content)

    # and save it to a file
    write_mp3_audio_file('victim.mp3', victim_tts.audio_content)

    # Play the audio file
    victim_play_audio_file('victim.mp3')