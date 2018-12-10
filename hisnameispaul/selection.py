import os

import cv2

if __name__ == '__main__':
    if not os.path.exists('selection'):
        os.mkdir('selection')

    img = cv2.imread('Exhibition18.jpg', 0)

    height, width = img.shape
    rectangles = [
        # (x1 y1) (x2 y2)
        ['full', 0, 0, width, height],
        ['muffins', 1520, 1100, 1920, 1380],
        ['blue_yellow', 640, 370, 1120, 820],
        ['black_white', 1120, 360, 1480, 820],
    ]

    for i, (name, x1, y1, x2, y2) in enumerate(rectangles):
        print(f'selection {i + 1}: {name} (({x1}, {y1}), ({x2}, {y2}))')

        cropped = img[y1:y2, x1:x2]

        cv2.imwrite(f'selection/{name}.jpg', cropped)
