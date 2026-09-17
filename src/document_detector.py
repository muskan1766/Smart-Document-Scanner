import cv2
import numpy as np


def detect_document(edges, image=None):
    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        _, mask = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT, (15, 15)
        )

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_CLOSE,
            kernel
        )

        mask = cv2.morphologyEx(
            mask,
            cv2.MORPH_OPEN,
            kernel
        )

        contours, _ = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        image_area = gray.shape[0] * gray.shape[1]

        for contour in sorted(
            contours,
            key=cv2.contourArea,
            reverse=True
        ):
            area = cv2.contourArea(contour)

            if area < image_area * 0.20:
                continue

            perimeter = cv2.arcLength(contour, True)

            approx = cv2.approxPolyDP(
                contour,
                0.03 * perimeter,
                True
            )

            if len(approx) == 4:
                return approx.reshape(4, 2)

    contours, _ = cv2.findContours(
        edges.copy(),
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    image_area = edges.shape[0] * edges.shape[1]

    for contour in sorted(
        contours,
        key=cv2.contourArea,
        reverse=True
    ):
        area = cv2.contourArea(contour)

        if area < image_area * 0.20:
            continue

        perimeter = cv2.arcLength(contour, True)

        approx = cv2.approxPolyDP(
            contour,
            0.03 * perimeter,
            True
        )

        if len(approx) == 4:
            return approx.reshape(4, 2)

    raise ValueError("Document boundary could not be detected.")