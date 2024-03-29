FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app
COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --no-cache-dir qrcode[pil]

ENTRYPOINT ["python", "main.py"]
CMD ["--url", "https://github.com/kaw393939"]
