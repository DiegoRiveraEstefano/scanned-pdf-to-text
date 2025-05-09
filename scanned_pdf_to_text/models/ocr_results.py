from dataclasses import dataclass


@dataclass
class OCRResult:
    text: str
    confidence: float
    page_num: int
    language: str