FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-devel

WORKDIR /app/

COPY ./main.py /app/
COPY ./requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN sh requirements.sh
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install libgl1-mesa-glx
RUN apt-get install libglib2.0-0