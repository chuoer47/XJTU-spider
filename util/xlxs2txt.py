"""
将xlxs文件转化为txt文件
"""
import os
import re

import pandas as pd


def sanitize_filename(filename):
    # 删除文件名中的无效字符
    return re.sub(r'[\\/*?:"<>|]', "", filename)


def xlsx_to_txt(input_file, output_folder):
    # 读取xlsx文件
    df = pd.read_excel(input_file)

    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历每一行数据
    for index, row in df.iterrows():
        # 从第一列获取标题
        title = str(row[0])
        sanitized_title = sanitize_filename(title)

        # 构造文件名，使用标题作为文件名
        filename = os.path.join(output_folder, f"{sanitized_title}.txt")

        # 将当前行的数据写入到txt文件中
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"标题: {row[0]}\n")  # 使用第一列作为标题
            f.write(f"发布日期: {row[1]}\n")  # 第二列是发布日期
            f.write(f"浏览次数: {row[2]}\n")  # 第三列是浏览次数
            f.write("正文内容:\n")
            f.write(str(row[3]))  # 第四列是正文内容

    print(f"已将xlsx文件转换为txt文件，存储在{output_folder}文件夹中。")
