from openpyxl import Workbook


def save_excel(result_list):
    wb = Workbook()
    sheet = wb.active
    try:
        for row in result_list:
            sheet.append(row)
            wb.save('./result/result.xlsx')
        return True,"./result/result.xlsx 保存成功！"
    except Exception as e:
        return False,f"result.xlsx 保存失败! ERROR:{e}"
