class WriterException(Exception):
    """Base exception for all Writer errors"""

class WriterConnectionError(WriterException):
    """Network-related errors"""

class WriterProcessingError(WriterException):
    """Processing failures"""

class WriterFormatError(WriterException):
    """Format-related errors"""

class WriterFileError(WriterException):
    """File-related errors"""

class WriterIOError(WriterException):
    """IO-related errors"""

class WriterValueError(WriterException):
    """Value-related errors"""