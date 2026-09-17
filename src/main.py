import argparse
import os
import cv2

from input_handler import load_image
from preprocessing import preprocess_image
from document_detector import detect_document
from perspective import perspective_transform
from enhancement import enhance_document
from output_handler import save_image


def scan_document(input_path, output_path, mode):
    print("Loading image...")
    image = load_image(input_path)

    print("Preprocessing image...")
    _, edges = preprocess_image(image)

    print("Detecting document boundary...")
    corners = detect_document(edges, image)

    preview = image.copy()
    cv2.polylines(
        preview,
        [corners.astype(int)],
        True,
        (0, 255, 0),
        4
    )

    preview_path = os.path.join(
        os.path.dirname(output_path),
        "detected_document.png"
    )

    save_image(preview, preview_path)

    print("Document detected.")

    print("Applying perspective correction...")
    scanned = perspective_transform(image, corners)

    print(f"Applying '{mode}' enhancement...")
    result = enhance_document(scanned, mode)

    save_image(result, output_path)

    print("\nScan completed successfully.")
    print(f"Detected boundary: {preview_path}")
    print(f"Scanned document: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Smart Document Scanner using Computer Vision"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input image"
    )

    parser.add_argument(
        "--output",
        default="data/output/scanned_document.png",
        help="Path to save the scanned document"
    )

    parser.add_argument(
        "--mode",
        choices=["original", "gray", "bw", "enhanced"],
        default="enhanced",
        help="Document enhancement mode"
    )

    args = parser.parse_args()

    try:
        scan_document(
            args.input,
            args.output,
            args.mode
        )
    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()