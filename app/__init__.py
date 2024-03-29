from .QRCode.generator import QRCodeGenerator, QRCodeApp
class App:
    def start():
        print("Generating QR Code...")
        qr_generator = QRCodeGenerator()
        app = QRCodeApp(qr_generator)
        app.create_qr("https://example.com", "qr_code.png")
