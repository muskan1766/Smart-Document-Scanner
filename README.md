# Smart Document Scanner Using Computer Vision

## Overview

Smart Document Scanner is a Python-based computer vision application that converts photographs of documents into clean, perspective-corrected digital scans.

The system detects the document boundary, corrects perspective distortion, and applies image enhancement techniques to produce a readable scanned document.

## Problem Statement

Photographs of documents are often captured at different angles and may contain perspective distortion, uneven lighting, and background noise. Manually correcting these images can be time-consuming.

This project provides an automated computer vision solution that detects the document region and transforms it into a properly aligned and enhanced scanned document.

## Objectives

- Detect the boundary of a document from an input image.
- Extract the document region using contour detection.
- Correct perspective distortion.
- Generate grayscale and black-and-white document versions.
- Enhance document readability.
- Save the processed document automatically.
- Provide a command-line interface for execution.

## Features

- Image input validation
- Grayscale conversion
- Gaussian blur
- Canny edge detection
- Morphological image processing
- Document contour detection
- Four-corner document extraction
- Perspective transformation
- Document enhancement
- Grayscale mode
- Black-and-white mode
- Automatic output generation
- Command-line execution
- Automated testing

## Technologies Used

- Python 3
- OpenCV
- NumPy
- Pytest
- Git
- GitHub

## Project Structure

```text
Smart-Document-Scanner/
│
├── data/
│   ├── input/
│   └── output/
│
├── docs/
│
├── src/
│   ├── main.py
│   ├── input_handler.py
│   ├── preprocessing.py
│   ├── document_detector.py
│   ├── perspective.py
│   ├── enhancement.py
│   └── output_handler.py
│
├── tests/
│   └── test_scanner.py
│
├── requirements.txt
├── README.md
├── statement.md
└── .gitignore
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/muskan1766/Smart-Document-Scanner.git
cd Smart-Document-Scanner
```

### 2. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Input Image

Place the document image inside:

```text
data/input/
```

Example:

```text
data/input/document.png
```

The application supports common image formats such as PNG, JPG, and JPEG.

## Running the Project

Run the scanner using:

```bash
python src/main.py --input data/input/document.png
```

The default enhancement mode is `enhanced`.

## Enhancement Modes

### Original

```bash
python src/main.py --input data/input/document.png --mode original
```

### Grayscale

```bash
python src/main.py --input data/input/document.png --mode gray
```

### Black and White

```bash
python src/main.py --input data/input/document.png --mode bw
```

### Enhanced

```bash
python src/main.py --input data/input/document.png --mode enhanced
```

## Output

The application generates two output files:

```text
data/output/detected_document.png
data/output/scanned_document.png
```

### Detected Document

`detected_document.png` shows the detected boundary of the document.

### Scanned Document

`scanned_document.png` contains the perspective-corrected and enhanced document.

## Computer Vision Pipeline

```text
Input Image
     |
     v
Image Preprocessing
     |
     v
Grayscale Conversion
     |
     v
Gaussian Blur
     |
     v
Canny Edge Detection
     |
     v
Contour Detection
     |
     v
Document Boundary Detection
     |
     v
Perspective Transformation
     |
     v
Image Enhancement
     |
     v
Scanned Document
```

## Testing

Run the automated tests using:

```bash
pytest tests -v
```

The tests cover:

- Image preprocessing
- Point ordering
- Grayscale enhancement
- Black-and-white enhancement

Expected result:

```text
4 passed
```

## Error Handling

The application handles:

- Missing input files
- Invalid image files
- Failure to detect a document boundary
- Invalid enhancement modes
- Output file errors

## Limitations

- The input image should contain a clearly visible document.
- Very low-light or heavily blurred images may reduce detection quality.
- Complex backgrounds may make document detection more difficult.
- The current system is designed primarily for single-document images.

## Future Enhancements

- Multi-page document scanning
- OCR-based text extraction
- Automatic PDF generation
- Automatic document orientation detection
- Shadow and noise removal
- Real-time camera scanning
- Mobile application integration
- Deep-learning-based document detection

## Project Purpose

This project demonstrates the practical application of computer vision techniques for automated document scanning and image transformation.