from app.convertors.image_to_pdf import convert_image_to_pdf
from app.convertors.pdf_to_image import convert_pdf_to_image
from app.enums.conversion_type import ConversionType
import os

class ConversionService:

    def __init__(self):

        self._dispatch = {
            ConversionType.IMG_TO_PDF: convert_image_to_pdf,
            ConversionType.PDF_TO_IMAGE: convert_pdf_to_image
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
        
        image_name = os.path.basename(input_file)[0]

        if conversion_type == ConversionType.IMG_TO_PDF:
            pdf_path = os.path.join(
                output_dir, f"{image_name}.pdf"
            )

            convert_image_to_pdf(input_file, pdf_path)

            return pdf_path
        
        elif conversion_type == ConversionType.PDF_TO_IMAGE:

            convert_pdf_to_image(input_file, output_dir)

            return output_dir

        else:
            raise ValueError("Unsupported converison")


