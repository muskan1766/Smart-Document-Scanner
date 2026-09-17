# Project Statement

## Project Title

Smart Document Scanner Using Computer Vision

## Problem Statement

Photographs of documents may contain perspective distortion, uneven lighting, background regions, and other visual imperfections. These issues can make photographed documents difficult to read, store, and use as digital documents.

The Smart Document Scanner provides an automated computer vision solution that detects the document boundary, corrects perspective distortion, and enhances the resulting image.

## Scope of the Project

The project focuses on scanning a single document from an input image using classical computer vision techniques.

The system performs the following operations:

- Image input and validation
- Image preprocessing
- Grayscale conversion
- Gaussian blurring
- Edge detection
- Contour detection
- Document boundary detection
- Perspective correction
- Image enhancement
- Output generation

The system is implemented as a command-line application.

## Target Users

The system can be useful for:

- Students
- Teachers
- Researchers
- Office users
- Individuals who want to digitize printed documents

## High-Level Features

1. Document image input
2. Image preprocessing
3. Document boundary detection
4. Contour-based document extraction
5. Perspective correction
6. Grayscale conversion
7. Black-and-white enhancement
8. Automatic output generation
9. Error handling
10. Command-line execution
11. Automated testing

## Functional Requirements

### FR1 - Image Input

The system shall accept a document image as input through the command line.

### FR2 - Image Preprocessing

The system shall preprocess the input image using grayscale conversion, Gaussian blur, Canny edge detection, and morphological operations.

### FR3 - Document Boundary Detection

The system shall identify the document boundary from the processed image using contour analysis.

### FR4 - Perspective Correction

The system shall transform the detected document into a rectangular, front-facing view.

### FR5 - Image Enhancement

The system shall provide different output modes including original, grayscale, black-and-white, and enhanced versions.

### FR6 - Output Generation

The system shall save the detected document boundary and final scanned document to the output directory.

### FR7 - Error Handling

The system shall provide meaningful error messages when the input is invalid or the document boundary cannot be detected.

## Non-Functional Requirements

### NFR1 - Performance

The system should process normal-sized document images within a reasonable amount of time.

### NFR2 - Usability

The application should provide simple command-line commands for scanning documents.

### NFR3 - Reliability

The system should handle invalid inputs and document-detection failures without unexpected termination.

### NFR4 - Maintainability

The application should be divided into separate modules for input handling, preprocessing, detection, perspective transformation, enhancement, and output handling.

### NFR5 - Resource Efficiency

The system should use lightweight computer vision techniques that can run on a standard computer without requiring specialized hardware.

### NFR6 - Error Handling

The system should display clear error messages for missing files, invalid images, unsupported modes, and unsuccessful document detection.

## Technical Approach

The project uses classical computer vision techniques implemented using Python and OpenCV.

The main processing pipeline is:

```text
Input Image
     |
     v
Preprocessing
     |
     v
Edge Detection
     |
     v
Contour Detection
     |
     v
Document Boundary
     |
     v
Perspective Transformation
     |
     v
Image Enhancement
     |
     v
Final Scanned Document
```

## Computer Vision Techniques Used

### Grayscale Conversion

The input image is converted from a color image into grayscale to simplify image processing.

### Gaussian Blur

Gaussian filtering is applied to reduce noise before edge detection.

### Canny Edge Detection

Canny edge detection is used to identify strong edges in the image.

### Contour Detection

Contours are analyzed to locate the boundary of the document.

### Perspective Transformation

The detected document boundary is transformed into a rectangular, front-facing view.

### Adaptive Thresholding

Adaptive thresholding is used to create an enhanced black-and-white document output.

## Software Requirements

- Python 3
- OpenCV
- NumPy
- Pytest
- VS Code or any Python-compatible IDE

## Hardware Requirements

- Standard computer or laptop
- Minimum 4 GB RAM
- Sufficient storage for project files and images

## Expected Output

The system should produce:

1. An image showing the detected document boundary.
2. A perspective-corrected document.
3. An enhanced scanned version of the document.

## Testing

The project includes automated tests for important processing components.

Testing covers:

- Image preprocessing
- Point ordering
- Grayscale enhancement
- Black-and-white enhancement

The current test suite contains four automated tests, and all tests pass successfully.

## Limitations

The system may have reduced performance when:

- The document boundary is unclear.
- The image contains excessive shadows.
- The document is heavily folded or occluded.
- The background has colors or patterns similar to the document.
- The input image is severely blurred.

## Future Enhancements

Future versions can include:

- OCR-based text extraction
- PDF generation
- Multi-page scanning
- Automatic shadow removal
- Real-time camera scanning
- Mobile application support
- Deep-learning-based document detection
- Automatic document orientation correction