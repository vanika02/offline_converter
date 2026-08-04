from app.convertors.image_to_pdf import convert_image_to_pdf
from app.convertors.pdf_to_image import convert_pdf_to_image
from PySide6.QtWidgets import QMessageBox
from app.utils.widgets.file_dialogs import SaveFileDialog

class ConversionService:

    def convert(self, input_file):

        if not input_file:
            QMessageBox.warning(
                self, "Error", "Please select a file"
            )
            return 
        
        output_dir = SaveFileDialog()

        if not output_dir:
            QMessageBox.warning(
                self, "Error", "No output directory"
            )
            return 
        
        conversion = self.conversion_box.currentText()

        try: 
            if conversion == "Image -> PDF":
                pdf_path = os.path.join(
                    output_dir, f"{image_name}.pdf"
                )

                convert_image_to_pdf(self.input_file, pdf_path)
            
            elif conversion == "PDF -> Image":

                convert_pdf_to_image(self.input_file, output_dir)

            if True:
                QMessageBox.information(
                    self, "Success", f"PDF created successfully!\n\n{pdf_path}"
                )
            
        except Exception as e:
            QMessageBox.critical(
                self, "Conversion failed", str(e)
            )

