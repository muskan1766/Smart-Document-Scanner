import cv2


def enhance_document(image, mode="enhanced"):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if mode == "original":
        return image

    if mode == "gray":
        return gray

    if mode == "bw":
        return cv2.adaptiveThreshold(
            gray,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            21,
            15
        )

    if mode == "enhanced":
        denoised = cv2.GaussianBlur(gray, (3, 3), 0)

        return cv2.adaptiveThreshold(
            denoised,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            21,
            12
        )

    raise ValueError(
        "Invalid mode. Choose original, gray, bw, or enhanced."
    )