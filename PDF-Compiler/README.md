# PDF Compiler

## Usage

Place the program inside a seperate directory and copy the images that you want to compile a PDF from.

Install `img2pdf` (this needs to be done only the first time):

- On terminals, use `python3 -m pip install img2pdf`
- On Android, your Python IDE (Pydroid) app should have an option to install PyPI (PIP) packages.

Run the program:

- On terminals, use `python3 pdf_compiler.py`
- On Android, open the program on your Python IDE (PyDroid) app and run it from there.

A PDF file called **document.pdf** will be compiled from all the images inside the directory.

## Logic

- Get all images from current folder
  - Get all the files from current folder
  - Filter out only the images
  - Sort images in required order
  - Check for all image extensions
- Compile those images into a PDF using img2pdf module
