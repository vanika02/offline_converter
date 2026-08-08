from PIL import Image
from pathlib import Path
from pdf2image import convert_from_path
import logging
from app.convertors.base_converter import BaseConverter

logger = logging.getLogger(__name__)

class PdfToImageConverter(BaseConverter):

    def convert(self, input_file: str, output_dir: str) -> str:
        """
        Convert every page of a PDF to PNG image.

        Args:
            input_file: Path to the input PDF.
            output_dir: Directory where the images will be saved.

        Returns:
            A list containing the paths of all generated images.
        """

        pdf_name = Path(input_file).stem
        pages = convert_from_path(input_file)

        output_files = []

        for index, page in enumerate(pages, start=1):
            output_path = Path(output_dir) / f"{pdf_name}_page_{index}.png"

            page.save(output_path, "PNG")

            output_files.append(str(output_path))

        logger.info(
            "Conversion completed successfully: %s",
            output_files,
        )

        logger.error(
            "Conversion failed",
            exec_info=True
        )
        return output_files