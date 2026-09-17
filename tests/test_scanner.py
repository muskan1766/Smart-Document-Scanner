import os
import sys
import cv2
import numpy as np

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../src")
    )
)

from preprocessing import preprocess_image
from perspective import order_points
from enhancement import enhance_document


def test_preprocessing():
    image = np.zeros((500, 500, 3), dtype=np.uint8)

    gray, edges = preprocess_image(image)

    assert gray.shape == (500, 500)
    assert edges.shape == (500, 500)


def test_order_points():
    points = np.array([
        [100, 100],
        [400, 100],
        [400, 400],
        [100, 400]
    ])

    result = order_points(points)

    assert result.shape == (4, 2)


def test_grayscale_enhancement():
    image = np.zeros((500, 500, 3), dtype=np.uint8)

    result = enhance_document(image, "gray")

    assert len(result.shape) == 2


def test_bw_enhancement():
    image = np.ones((500, 500, 3), dtype=np.uint8) * 255

    result = enhance_document(image, "bw")

    assert result.shape == (500, 500)