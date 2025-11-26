import runpod
from analyze_handler import analyze_audio_url

def handler(job):
    try:
        url = job["input"].get("audio_url")
        if not url:
            return {"error": "No audio_url provided"}

        print(f"🎧 Processing URL: {url}")

        text = analyze_audio_url(url)

        return {"transcription": text}

    except Exception as e:
        return {"error": str(e)}

runpod.serverless.start({"handler": handler})