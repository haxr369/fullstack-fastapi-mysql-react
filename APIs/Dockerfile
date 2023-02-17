FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-devel

WORKDIR /app/

COPY ./main.py /app/
COPY ./requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt