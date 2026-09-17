import cv2
import os


def save_image(image, output_path):
    directory = os.path.dirname(output_path)

    if directory:
        os.makedirs(directory, exist_ok=True)

    success = cv2.imwrite(output_path, image)

    if not success:
        raise ValueError("Unable to save output image.")

    return output_path