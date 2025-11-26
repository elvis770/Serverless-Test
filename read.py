import requests
import uuid
import os

def download_audio(url):
    # Generate unique filename
    filename = f"audio_{uuid.uuid4().hex}.mp3"
    filepath = f"/workspace/{filename}"

    # Download audio
    r = requests.get(url)
    if r.status_code != 200:
        raise ValueError("Could not download audio file")

    # Save file
    with open(filepath, "wb") as f:
        f.write(r.content)

    return filepath