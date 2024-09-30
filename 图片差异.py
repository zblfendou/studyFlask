import cv2
import numpy as np
from scipy.fftpack import dct


def dct_similarity(img1_path, img2_path):
    # 使用 OpenCV 读取图像并转换为灰度
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    # 对图像进行离散余弦变换
    dct1 = dct(dct(img1, axis=0, norm='ortho'), axis=1, norm='ortho')
    dct2 = dct(dct(img2, axis=0, norm='ortho'), axis=1, norm='ortho')

    # 计算 DCT 差异（欧氏距离）
    diff = np.linalg.norm(dct1 - dct2)
    return diff


dct_diff = dct_similarity('static/1.png', 'static/2.png')
print(f"两张图片的 DCT 差异: {dct_diff}")
