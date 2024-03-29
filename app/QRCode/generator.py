import qrcode
from abc import ABC, abstractmethod

class QRCodeGeneratorInterface(ABC):
    @abstractmethod
    def generate(self, data: str, path: str) -> None:
        pass

class QRCodeGenerator(QRCodeGeneratorInterface):
    def generate(self, data: str, path: str) -> None:
        img = qrcode.make(data)
        img.save(path)

class QRCodeApp:
    def __init__(self, generator: QRCodeGeneratorInterface):
        self.generator = generator

    def create_qr(self, data: str, output_path: str) -> None:
        self.generator.generate(data, output_path)