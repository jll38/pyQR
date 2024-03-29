import os
from .QRCode.generator import QRCodeGenerator, QRCodeApp
class App:
    def start():
        # Read environment variables or use default values
        qr_data_url = os.getenv('QR_DATA_URL', 'https://example.com')
        qr_code_filename = os.getenv('QR_CODE_FILENAME', 'qr_code.png')

        print("Generating QR Code...")
        qr_generator = QRCodeGenerator()
        app = QRCodeApp(qr_generator)
        app.create_qr(qr_data_url, qr_code_filename)