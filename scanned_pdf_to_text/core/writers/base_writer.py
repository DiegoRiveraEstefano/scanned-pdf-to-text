from abc import abstractmethod, ABC
from scanned_pdf_to_text.models.ocr_results import OCRResult

class BaseWriter(ABC):


    @abstractmethod
    def open(self, file_path: str):
        """ Opens the file for writing, creating the necessary directories if needed.

        Args:
            file_path (str): The path to the file to be written.
        """
        raise NotImplementedError

    @abstractmethod
    def write(self, ocr_result: OCRResult):
        """ Writes the text to the file.

        Args:
            ocr_result (OCRResult): The OCR result to be written.
        Raises:
            NotImplementedError: If the method is not implemented.
            ValueError: If the file is not open.
            IOError: If an error occurs while writing to the file.
            TypeError: If the ocr_result is not of type OCRResult.
        """
        raise NotImplementedError

    @abstractmethod
    def close(self):
        raise NotImplementedError