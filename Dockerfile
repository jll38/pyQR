FROM python:3.9

WORKDIR /usr/src/app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN mkdir qr_codes

ENV QR_DATA_URL="https://github.com/kaw393939"
ENV QR_CODE_FILENAME="qr_codes/github_qr.png"

CMD ["python", "main.py"]
