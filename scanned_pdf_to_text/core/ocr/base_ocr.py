from abc import ABC, abstractmethod

class BaseOCR(ABC):
    @abstractmethod
    def process_image(self, image: Image, lang: str = 'eng') -> OCRResult:
        pass