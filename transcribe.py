import whisperx
import torch

model = None

def load_model():
    global model
    if model is None:
        print("🧠 Loading WhisperX model on GPU...")
        model = whisperx.load_model("large-v3", device="cuda")
    return model

def transcribe_audio(audio_path):
    model = load_model()
    result = model.transcribe(audio_path)
    return result["text"]