class OCRFactory:
    _implementations = {
        'tesseract': TesseractOCR,
        'google-vision': GoogleVisionOCR,
        'aws-textract': AWSTextractOCR
    }

    @classmethod
    def create_engine(cls, engine_name: str) -> BaseOCR:
        return cls._implementations[engine_name]()