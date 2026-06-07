## Offline File Converter

A privacy-first desktop application built ith Python and PySide6

The application performs file conversions locally on the user's machine without uploading files to any third-party server.


## Folder Structure

```
/home/vanika/offline_converter/app
├── __init__.py
├── assets
│   └── icons
│       └── button.svg
├── convertors
│   └── image_to_pdf.py
├── main.py
├── ui
│   ├── __init__.py
│   ├── layout_colorwidget.py
│   └── main_window.py
└── utils
    ├── __init__.py
    └── file_dialogs.py

7 directories, 11 files

```

## Current Features 

### 1. Image -> PDF conversion
- Select image files
- convert images to pdf
- Choose output folder
- Local processing 
- No cloud uploads

All conversions happen offline.

## Tech Stack

- Python
- PySide6
- Pillow
- img2pdf

## Installation

Clone the repository:

```
git clone https://github.com/vanika02/offline_converter.git
cd offline_converter
```
