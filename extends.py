import glob
import os,shutil
from config import logger
import zipfile
import base64

def initialize_directory(directorys=[]):
    """
    初始化目录
    :param directory: 如果需要额外创建其他目录
    :return:
    """

    # 删除当前目录下的所有img文件
    img_exists_files = glob.glob('./*.jpg') + glob.glob('./*.png') + glob.glob('./*.jpeg')
    for img_exists in img_exists_files:
        os.remove(img_exists)


    if os.path.exists('result'):
        shutil.rmtree('./result')
        logger.info("删除result")
    else:
        os.mkdir('./result')
        logger.info("创建result目录完成")
        os.mkdir('./result/right')
        logger.info("创建./result/right目录完成")
        os.mkdir('./result/wrong')
        logger.info("创建./result/right目录完成")

    if  os.path.exists('result.zip'):
        os.remove('result.zip')
        logger.info("删除result.zip")

    if not os.path.exists('./log'):
        os.mkdir('log')
        logger.info("创建log目录完成")



    if directorys:
        for directory in directorys:
            if not os.path.exists(directory):
                os.mkdir(directory)
                logger.info(f"创建{directory}目录完成")



def move_file(imgfile, dstpath):
    """
    :param imgfile: 需要复制、移动的文件
    :param dstpath: 目的地址
    :return:
    """
    if not os.path.isfile(imgfile):
        logger.error(f"{imgfile} not exist!" )
    else:
        fpath, fname = os.path.split(imgfile)  # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.move(imgfile, dstpath + fname)  # 复制文件
        logger.info(f"MOVE {imgfile} --> {dstpath + fname}")



def zip_directory(directory_path, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory_path)
                zipf.write(file_path, arcname)
                print(f"{file} -> {zip_filename}")

