from pathlib import Path

from PIL import Image
import img2pdf


def convert_image_to_pdf(input_file: str, output_dir: str) -> str:
    """
    Convert an image to PDF.

    Args:
        input_file: Path to the input image.
        output_dir: Directory where the PDF should be saved.
    
    Returns:
        Path to the created PDF.
    """

    image_name = Path(input_file).stem
    output_path = Path(output_dir) / f"{image_name}.pdf"

    with Image.open(input_file) as image:
        pdf_bytes = img2pdf.convert(image.filename)
    
    with open(output_path, "wb") as file:
        file.write(pdf_bytes)

    return str(output_path)