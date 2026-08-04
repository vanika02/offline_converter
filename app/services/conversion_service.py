from app.convertors.image_to_pdf import convert_image_to_pdf
from app.convertors.pdf_to_image import convert_pdf_to_image
import os

class ConversionService:

    def convert(self, input_file, output_dir, conversion_type):

        if not input_file:
            raise ValueError("Please select a file")
            return 
        
        if not output_dir:
            raise ValueError("No output directory selected")
            return      

        if conversion_type == "Image -> PDF":
            pdf_path = os.path.join(
                output_dir, f"{image_name}.pdf"
            )

            convert_image_to_pdf(input_file, pdf_path)
        
        elif conversion_type == "PDF -> Image":

            convert_pdf_to_image(input_file, output_dir)

        else:
            raise ValueError("Unsupported converison")


