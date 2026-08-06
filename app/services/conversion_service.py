from app.convertors.image_to_pdf import convert_image_to_pdf
from app.convertors.pdf_to_image import convert_pdf_to_image
from app.conversion_type import ConversionType
import os

class ConversionService:

    def convert(
        self,
        input_file: str, 
        output_dir: str, 
        conversion_type: str) -> str:

        if not input_file:
            raise ValueError("Please select a file")
        
        if not output_dir:
            raise ValueError("No output directory selected")
        
        image_name = os.path.basename(input_file)[0]

        enum_conversion = ConversionService()
        if conversion_type == enum_conversion.IMG_TO_PDF:
            pdf_path = os.path.join(
                output_dir, f"{image_name}.pdf"
            )

            convert_image_to_pdf(input_file, pdf_path)

            return pdf_path
        
        elif conversion_type == enum_conversion.PDF_TO_IMAGE:

            convert_pdf_to_image(input_file, output_dir)

            return output_dir

        else:
            raise ValueError("Unsupported converison")


