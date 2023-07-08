import config
from PIL import Image,ImageDraw,ImageFont
import os

tfont = ImageFont.truetype(r'C://Windows/SIMYOU.TTF',18)
wrong = Image.open('source/wrong.jpg')
right = Image.open('source/right.jpg')

from PIL import Image
import os

from PIL import Image
import os


def convert_to_jpg(image_path):
    # 获取图像文件名和所在目录
    image_dir, image_filename = os.path.split(image_path)
    # 构建输出文件的完整路径
    output_path = os.path.join(image_dir, os.path.splitext(image_filename)[0] + ".jpg")

    # 打开图像并转换为RGB模式
    image = Image.open(image_path)
    rgb_image = image.convert("RGB")

    # 保存为JPG格式
    rgb_image.save(output_path, "JPEG")
    # 删除源文件
    os.remove(image_path)

    config.logger.info(f"{image_path} Converted to {output_path}")
    return output_path




def wrong_img(img_path,msg):
    with Image.open(img_path) as img_file:  # 通过Image库打开img文件
        img_file.paste(wrong, (0, 0))  # 添加不合规的jpg
        drawer = ImageDraw.Draw(img_file)  # 读取image文件file
        drawer.text((0, 0), msg, fill=(255, 0, 0), font=tfont)  # 添加文本
        img_file.save(img_path)  # 存储覆盖原来的文件

if __name__ == '__main__':
    convert_to_jpg('./source/right.jpg')

