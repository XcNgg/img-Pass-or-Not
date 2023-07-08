from config import APP_ID,API_KEY,SECRET_KEY
from aip import AipImageCensor # pip install baidu-aip


CLIENT = AipImageCensor(APP_ID,API_KEY,SECRET_KEY)

def get_img_result(img_path):
    with open(img_path, 'rb') as i:
        #  获取img的编码信息
        imginfo = i.read()
    result = CLIENT.imageCensorUserDefined(imginfo)  # 调用接口审核信息
    return result


