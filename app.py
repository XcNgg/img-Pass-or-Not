# encoding:utf-8
import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from extends import initialize_directory, zip_directory, move_file
from AI_SDK import get_img_result
from config import logger
from img_process import wrong_img,convert_to_jpg
from saver import save_excel


# app = Flask(__name__,static_folder='templates/static', static_url_path='/static', )
app = Flask(__name__ )

# static_folder 参数用于指定静态文件的文件夹路径。
# static_folder='templates/static' 表示静态文件存放在 "templates/static" 文件夹下。
# "static" 文件夹位于 "templates" 文件夹下。

# static_url_path 参数用于指定静态文件的 URL 路径。
# static_url_path='/static' 表示静态文件的 URL 路径为 "/static"。
# 也就是说，当浏览器请求静态文件时，路径将以 "/static" 开头，
# "/static/css/style.css" 或 "/static/img/logo.png"。


def examine():
    # 初始化目录
    initialize_directory()

    # 设置表格的表头
    result_list = [['原文件名', '结论', '可能问题']]

    # 获取上传的图像文件
    img_files = request.files.getlist('imageUpload')



    for img_file in img_files:

        # 获取图像文件路径
        img_path = img_file.filename

        # 保存图像文件
        img_file.save(img_path)

        # 判断图像是否不是jpg格式
        if os.path.splitext(img_file.filename)[-1] != 'jpg':
            # 如果非jpg格式，将图像转为Jpg格式
            img_path = convert_to_jpg(img_file.filename)



        # 调用 AI_SDK 进行图像审核
        logger.info(f"正在审核 {img_path}")

        img_result = get_img_result(img_path=img_path)
        conclusion = img_result['conclusion']

        # 如果图像不合规
        if conclusion == '不合规' or conclusion == '疑似':
            msg = img_result['data'][0]['msg']
            logger.error(img_path + " | " + conclusion)
            result_list.append([img_path, conclusion, msg])

            # 处理不合规的图像
            wrong_img(img_path=img_path, msg=msg)
            move_file(img_path, './result/wrong/')

        # 如果图像合规
        else:
            logger.info(img_path + " | " + conclusion)
            result_list.append([img_path, conclusion, '合规'])
            move_file(img_path, './result/right/')

        # 将审核结果保存为 Excel 文件
        excel_result = save_excel(result_list=result_list)
        if excel_result[0]:
            logger.info(excel_result[1])
        else:
            logger.error(excel_result[1])

    # 压缩审核结果目录
    zip_directory('./result', 'result.zip')

    return '审核完成,点击下载结果'



@app.route('/', methods=['GET'])
def index():
    # 初始化目录
    result = request.args.get('result')  # 从查询参数中检索result的值
    return render_template('index.html', result=result)


@app.route('/upload', methods=['POST', 'GET'])
def upload_result():
    if request.method == 'POST':
        result = examine()
        return redirect(url_for('index', result=result))  # 重定向到/index页面，并将结果作为参数传递
    else:
        return "违法请求！"

@app.route('/download', methods=['GET'])
def download_excel():
    if os.path.exists('result.zip'):
        return send_file('result.zip', as_attachment=True)
    else:
        return render_template('index.html', result="当前不存在结果，请上传审核文件")

if __name__ == "__main__":
    app.run()
