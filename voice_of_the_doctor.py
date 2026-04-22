import os
from gtts import gTTS
from elevenlabs import ElevenLabs

# --- GOOGLE TTS PART (gTTS) ---
def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

# input_text = "hi there it's Ahraz pls speak something!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")



client = ElevenLabs(api_key="eleven labs api key")

def text_to_speech_elevenlabs_old(input_text, output_filepath="output.mp3"):
    # Audio chunks generate karo
    audio_stream = client.text_to_speech.convert(
        voice_id="EXAVITQu4vr4xnSDxMaL",  # Default voice (Rachel)
        model_id="eleven_turbo_v2",
        text=input_text
    )

    # File save karo
    with open(output_filepath, "wb") as f:
        for chunk in audio_stream:   # Har chunk likho
            f.write(chunk)

# Example run
#text_to_speech_elevenlabs_old(input_text, "elevenlabs_testing.mp3")

#step 2
# this created becuse the microphone automatically connected to my speaker sytem to make a speech
# us the text model for text output for voice
import subprocess
import platform
def text_to_speech_with_gtts(input_text, output_filepath="gtts_testing.mp3"):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

    # Play audio file according to OS
    os_name = platform.system()
    try:
        if os_name == "Windows":  # Windows
            os.startfile(output_filepath)   # Default player se play karega
        elif os_name == "Darwin":  # macOS
            subprocess.run(['open', output_filepath])
        elif os_name == "Linux":  # Linux
            subprocess.run(['xdg-open', output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


# --- ELEVENLABS TTS PART ---
client = ElevenLabs(api_key="api key")

def text_to_speech_elevenlabs(input_text, output_filepath="elevenlabs_testing.mp3"):
    audio_stream = client.text_to_speech.convert(
        voice_id="EXAVITQu4vr4xnSDxMaL",  # Default voice (Rachel)
        model_id="eleven_turbo_v2",
        text=input_text
    )

    with open(output_filepath, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    # Play audio file
    os_name = platform.system()#if u want to know the sytem which you are working
    try:
        if os_name == "Windows":
            os.startfile(output_filepath)
        elif os_name == "Darwin":
            subprocess.run(['open', output_filepath])
        elif os_name == "Linux":
            subprocess.run(['xdg-open', output_filepath])
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


# --- Example Run --- hre
input_text = "Hi there, it's Ahraz speaking autoplay from my chatbot!"
# text_to_speech_with_gtts(input_text)       # gTTS playback
# text_to_speech_elevenlabs(input_text)    # ElevenLabs playback