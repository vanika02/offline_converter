from app.convertors.image_to_pdf import ImageToPdfConverter
from app.convertors.pdf_to_image import PdfToImageConverter
from app.enums.conversion_type import ConversionType
import os

class ConversionService:

    def __init__(self):

        self._dispatch = {
            ConversionType.IMG_TO_PDF: ImageToPdfConverter(),
            ConversionType.PDF_TO_IMAGE: PdfToImageConverter()
        }

    def convert(
        self,
        input_file: str, 
        output_dir: str, 
        conversion_type: ConversionType) -> str:

        if not input_file:
            raise ValueError("Please select a file")
        
        if not output_dir:
            raise ValueError("No output directory selected")
        
        converter = self._dispatch.get[conversion_type]

        if converter is None:
            raise ValueError("Unsupported conversion type")
        
        return converter(input_file, output_dir)


