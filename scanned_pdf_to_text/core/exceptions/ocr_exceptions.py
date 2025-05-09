class OCRException(Exception):
    """Base exception for all OCR errors"""

class OCRConnectionError(OCRException):
    """Network-related errors"""

class OCRProcessingError(OCRException):
    """Processing failures"""