#### **README.md**
# Image Format Converter

A simple Python-based utility to convert images between various formats using the Pillow library. 

## Features
- Converts images to popular formats such as PNG, JPEG, BMP, WEBP, GIF, and TIFF.
- Interactive command-line prompts for user-friendly operation.
- Isolated dependencies with a virtual environment.

## Prerequisites
- Python 3.x installed on your system.
- Basic familiarity with the command line.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sarvinshrivastava/image-format-converter.git
   cd image-format-converter
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   # Windows
   .\env\Scripts\activate
   # macOS/Linux
   source env/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Activate the virtual environment:
   ```bash
   # Windows
   .\env\Scripts\activate
   # macOS/Linux
   source env/bin/activate
   ```

2. Run the script:
   ```bash
   python converterScript.py
   ```

3. Follow the prompts to:
   - Input the path to the image file.
   - Choose the desired output format.

## Example

```plaintext
Welcome to the Image Format Converter!

Please enter the path to your image file:
>>> example.jpg

Image loaded successfully!

Available formats: PNG, JPEG, JPG, BMP, WEBP, GIF, TIFF
Enter the desired format for the image:
>>> WEBP

Image successfully converted to WEBP!
Saved at: example_converted.webp
```