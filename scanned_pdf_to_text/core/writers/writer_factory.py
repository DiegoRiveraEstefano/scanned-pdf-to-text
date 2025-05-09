from scanned_pdf_to_text.core.exceptions.writer_exceptions import WriterValueError
from scanned_pdf_to_text.core.writers.base_writer import BaseWriter
from scanned_pdf_to_text.core.writers.implementations.console_writer import ConsoleWriter
from scanned_pdf_to_text.core.writers.implementations.docx_writer import DocxWriter
from scanned_pdf_to_text.core.writers.implementations.txt_writer import TextWriter
from scanned_pdf_to_text.core.writers.implementations.md_writer import MdWriter


class WriterFactory:
    _formats = {
        'txt': TextWriter,
        'docx': DocxWriter,
        'md': MdWriter,
        'console': ConsoleWriter
    }

    @classmethod
    def get_writer(cls, format: str) -> BaseWriter:
        if format not in cls._formats:
            raise WriterValueError(f"Format {format} not supported")
        return cls._formats[format]()