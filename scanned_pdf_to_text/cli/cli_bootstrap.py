from scanned_pdf_to_text.core.writers.writer_factory import WriterFactory
from scanned_pdf_to_text.core.ocr.ocr_factory import OCRFactory

class CLIBootstrap:
    """Cli tool to convert scanned pdf to text
    commands are:
    convert-pdf-to-text scan
    convert-pdf-to-text bulk_scan
    """

    def scan(self, input_path: str, output_path: str, lang: str = 'eng', engine: str = 'tesseract', writer: str = 'txt'):
        """Convert a single pdf to text
        Args:
            input_path (str): Path to the input pdf
            output_path (str): Path to the output text file
            lang (str, optional): Language to use for OCR. Defaults to 'eng'.
            engine (str, optional): OCR engine to use. Defaults to 'tesseract'.
            writer (str, optional): Format to write the output. Defaults to 'txt'.
        """
        writer_engine = WriterFactory.get_writer(writer)
        ocr = OCRFactory.create_engine(engine)
        ocr_result = ocr.process_image(input_path, lang)

    def bulk_scan(self, input_path: str, output_path: str, file_pattern: str = '*.pdf', lang: str = 'eng', engine: str = 'tesseract', writer: str = 'txt'):
        """Convert a directory of pdfs to text
        Args:
            input_path (str): Path to the input directory
            output_path (str): Path to the output directory
            file_pattern (str, optional): Pattern to match the files. Defaults to '*.pdf'.
            lang (str, optional): Language to use for OCR. Defaults to 'eng'.
            engine (str, optional): OCR engine to use. Defaults to 'tesseract'.
            writer (str, optional): Format to write the output. Defaults to 'txt'.
        """