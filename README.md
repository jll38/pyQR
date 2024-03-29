# IS421 QRCode Generator

This project is a containerized python application that will generate a QR Code based on user input.

Example usage:

```
docker build -t qr-code-generator .
```

```
docker run -d --name qr-generator \ -e QR_DATA_URL='https://github.com/jll38/pyQR/blob/main/README.md' \ -e QR_CODE_FILENAME='qr_codes/your_qr_code.png' \ -v $(pwd)/qr_codes:/usr/src/app/qr_codes \ qr-code-generator
```

Output:
<img src="./qr_codes/your_qr_code.png">