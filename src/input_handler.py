import cv2
import os


def load_image(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image not found: {path}")

    image = cv2.imread(path)

    if image is None:
        raise ValueError("Unable to read the image.")

    return image