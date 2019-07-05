FROM python:3.7

WORKDIR /usr/src/slide_client
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python3.7", "get_images.py"]