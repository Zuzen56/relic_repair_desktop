import cv2
import numpy as np
import random

# 读取图片
image_path = "image1_output_0.png"  # 请将"your_image.jpg"替换为您的图片路径
img = cv2.imread(image_path)

# 创建与图片尺寸相同的随机颜色遮罩
mask = np.zeros_like(img)
mask[:] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# 将遮罩融合到原始图片
blended = cv2.addWeighted(img, 0.5, mask, 0.5, 0)

# 显示结果
cv2.imshow('Result', blended)
cv2.waitKey(0)
cv2.destroyAllWindows()
