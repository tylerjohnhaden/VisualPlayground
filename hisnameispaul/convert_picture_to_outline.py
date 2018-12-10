import cv2
# import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Exhibition18.jpg', 0)

height, width = img.shape

rectangles = [
    # x1 y1 x2 y2
    ['muffins', 1520, 1100, 1920, 1380],
    ['blue & yellow', 640, 370, 1120, 820],

    ['black & white', 1120, 360, 1480, 820],

    ['full', 0, 0, width, height],
]

lower_threshold = 100
upper_threshold = 3 * lower_threshold

fig, axes = plt.subplots(2, len(rectangles))
CMAP = 'gray'

for i, (name, x1, y1, x2, y2) in enumerate(rectangles):
    print(1 + i, '******')
    print(name, x1, y1, x2, y2)

    cropped = img[y1:y2, x1:x2]

    axes[0, i].imshow(cropped, cmap=CMAP)
    axes[1, i].imshow(cv2.Canny(cropped, lower_threshold, upper_threshold), cmap=CMAP)

    axes[0, i].axes.set_title(name)

for i_ in range(len(axes)):
    for j_ in range(len(axes[0])):
        axes[i_, j_].axes.get_xaxis().set_visible(False)
        axes[i_, j_].axes.get_yaxis().set_visible(False)

plt.show()

# thing = 2
# for i in range(thing):
#     for j in range(thing):
#         crop_img = img[y:y + h, x:x + w]
#         lower_threshold = (j + (i * thing)) * 10
#         upper_threshold = 3 * lower_threshold
#         # upper_threshold = 200
#         print('i = {}, j = {}, order = {}'.format(lower_threshold, upper_threshold, (j + (i * thing))))
#         edges = cv2.Canny(img, lower_threshold, upper_threshold)
#         plt.subplot(thing, thing, 1 + (j + (i * thing))), plt.imshow(edges, cmap='gray')
#         plt.title('[{}, {}]'.format(lower_threshold, upper_threshold)), plt.xticks([]), plt.yticks([])
# plt.show()

# # Output dtype = cv2.CV_8U
# sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
#
# # Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
# sobelx64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
# abs_sobel64f = np.absolute(sobelx64f)
# sobel_8u = np.uint8(abs_sobel64f)
#
# custom = cv2.Laplacian(img, cv2.CV_16S)
# # custom = cv2.Laplacian(img, cv2.CV_64F)
# print(np.percentile(custom, [0, 25, 50, 75, 100]))
# print(np.mean(custom), np.std(custom))
#
# plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2, 2, 2), plt.imshow(sobelx8u, cmap='gray')
# plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
# plt.subplot(2, 2, 3), plt.imshow(sobel_8u, cmap='gray')
# plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
# plt.subplot(2, 2, 4), plt.imshow(custom, cmap='gray')
# plt.title('Custom'), plt.xticks([]), plt.yticks([])
#
#
# plt.show()
