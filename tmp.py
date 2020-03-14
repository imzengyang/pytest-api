import json
from openpyxl import Workbook
# 实例化Workbook 对象
workbook = Workbook()
# 创建一个 sheet
worksheet = workbook.active
# 单元格设置值
worksheet['A1'] = "编号"
worksheet['B1'] = '请求路径'
worksheet['C1'] = '请求方法'
worksheet['D1'] = '请求数据'
worksheet['E1'] = '其它参数'
worksheet['F1'] = '期望结果'

data = {
    "limit":1,
    "page":1
}
for x in range(1,4):
    worksheet.append((x,'http://39.107.96.138:3000/api/v1/topics','get',json.dumps(data),None,None))


# 更改 sheet 名字
worksheet.title = 'API'

workbook.save(filename='data/data.xlsx')