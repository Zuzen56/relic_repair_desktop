from PIL import Image, ImageFilter
import random

# 读取原始图片
img = Image.open('your_image_file.jpg')

# 定义破损函数
def apply_glitch(image, intensity=1):
    width, height = image.size
    data = image.load()
    for y in range(height):
        for x in range(width):
            if random.random() < 0.1 * intensity:  # 以10%的概率应用破损效果
                data[x, y] = (0, 0, 0)  # 将像素点设为黑色

# 添加破损效果
apply_glitch(img, intensity=3)  # 这里的intensity可以控制破损的程度

# 保存处理后的图片
img.save('glitched_image.jpg')