from scanned_pdf_to_text.core.writers.base_writer import BaseWriter
from scanned_pdf_to_text.models.ocr_results import OCRResult

class TextWriter(BaseWriter):
    
    def __init__(self):
        pass

    def open(self, file_path: str):
        pass

    def write(self, ocr_result: OCRResult):
        pass

    def close(self):
        pass