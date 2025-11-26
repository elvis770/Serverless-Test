from read import download_audio
from transcribe import transcribe_audio

def analyze_audio_url(url):
    print(f"🔽 Downloading: {url}")
    audio_path = download_audio(url)

    print(f"🎤 Transcribing audio: {audio_path}")
    text = transcribe_audio(audio_path)

    return text