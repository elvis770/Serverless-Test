FROM nvidia/cuda:12.1.0-runtime-ubuntu22.04

RUN apt-get update && apt-get install -y python3 python3-pip ffmpeg

RUN pip3 install --upgrade pip

RUN pip3 install torch==2.1.2 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

RUN pip3 install whisperx runpod requests numpy soundfile librosa

WORKDIR /workspace

COPY . /workspace

CMD ["python3", "rp_handler.py"]