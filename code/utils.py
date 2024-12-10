'''
千牛工作台的表情包分组导出为emo格式，emo后缀改为zip解压后则是一个存储着不同分组的表情包的目录
该文件用于配置分组目录下的EmotionConfig.json文件
手动任意文件名的创建含有'shortCut', 'meaning', 'originalFile'三个列的xls或xlsx表格，根据该文件生成EmotionConfig.json文件
'''

import os
import json
import pandas as pd
from glob import glob
import zipfile
import shutil
from pathlib import Path

def check_files(directory, exts):
    """检查目录下是否存在指定扩展名的文件"""
    files = []
    for ext in exts:
        files.extend(glob(os.path.join(directory, f'*.{ext}')))
    return files

def validate_excel(df, strictness=1):
    """验证Excel文件格式是否正确"""
    required_columns = ['shortCut', 'meaning', 'originalFile']
    
    if not all(col in df.columns for col in required_columns):
        print("表格式错误：缺少必要的列")
        exit(1)
    
    if strictness >= 1:
        for col in required_columns:
            if df[col].isnull().any():
                print(f"表格式错误：{col} 列存在空值")
                exit(1)
    
    if strictness == 2:
        if df.duplicated(subset=required_columns).any():
            print("表格式错误：存在重复项")
            exit(1)

def manage_config_json(directory, mode='new', strictness=1):
    """管理EmotionConfig.json文件"""

    # 判断directory变量是否为空
    if not directory:
        print("目录不能为空")
        return None

    # 判断directory是否存在
    if not os.path.exists(directory):
        print(f"目录 {directory} 不存在")
        return None

    excel_files = check_files(directory, ['xls', 'xlsx'])
    if not excel_files:
        print("找不到表配置文件")
        return None
    
    df = pd.read_excel(excel_files[0])
    validate_excel(df, strictness)
    
    image_files = check_files(directory, ['png', 'jpg'])
    if not image_files:
        print("没有图片文件")
        return None
    
    config_path = os.path.join(directory, 'EmotionConfig.json')
    if mode == 'new':
        if os.path.exists(config_path):
            os.remove(config_path)
        data = []
    elif mode == 'append':
        if os.path.exists(config_path):
            with open(config_path, 'r') as file:
                data = json.load(file)
        else:
            data = []
            mode = 'new'

    for index, row in df.iterrows():
        original_file = next((img for img in image_files if row['originalFile'] in img), None)
        if not original_file:
            print(f"未找到与 {row['originalFile']} 对应的图片文件")
            continue
        
        entry = {
            "shortCut": str(row['shortCut']),
            "meaning": str(row['meaning']),
            "originalFile": os.path.basename(original_file)
        }
        if mode == 'new' or entry not in data:
            data.append(entry)

    with open(config_path, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"成功生成 {config_path}")
    return True

# def json_to_xlsx(output_path='output.xlsx'):
#     """将config.json保存为xlsx文件"""

#     # json_path默认为当前目录下的文件
#     json_path = os.path.join(os.getcwd(), 'EmotionConfig.json')  # 使用完整路径

#     # 判断json_path是否存在
#     if not os.path.exists(json_path):
#         print(f"文件 {json_path} 不存在")
#         return None
    
#     # 读取JSON文件内容
#     with open(json_path, 'r') as file:
#         data = json.load(file)
    
#     df = pd.DataFrame(data)
#     df.to_excel(output_path, index=False)


def compress_to_emo(directory, file_name, output_filename="CustomEmo"):
    """将指定目录下的内容压缩为.zip并重命名为.emo"""

    # 判断directory变量是否为空
    if not directory:
        print("目录不能为空")
        exit(1)

    # 判断directory是否存在
    if not os.path.exists(directory):
        print(f"目录 {directory} 不存在")
        exit(1)

    # 构造要压缩的文件夹路径
    target_dir = os.path.join(directory, file_name)
    
    # 检查目标文件夹是否存在
    if not os.path.exists(target_dir):
        print(f"目标文件夹 {target_dir} 不存在")
        exit(1)

    # 判断是否存在output_filename.zip文件
    if os.path.exists(os.path.join(directory, f'{output_filename}.zip')):
        # 删除output_filename.zip文件
        os.remove(os.path.join(directory, f'{output_filename}.zip'))

    # 判断是否存在output_filename.emo文件
    if os.path.exists(os.path.join(directory, f'{output_filename}.emo')):
        # 删除output_filename.emo文件
        os.remove(os.path.join(directory, f'{output_filename}.emo'))

    # 创建临时ZIP文件路径
    zip_filename = os.path.join(directory, f'{output_filename}.zip')
    
    # 使用zipfile库创建压缩包
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 遍历目标文件夹中的所有文件和子文件夹
        for root, _, files in os.walk(target_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, target_dir)  # 保留相对路径
                zipf.write(file_path, arcname)

    # 构造最终输出文件路径（.emo）
    emo_filename = os.path.join(directory, f'{output_filename}.emo')

    # 将临时ZIP文件重命名为.emo
    os.rename(zip_filename, emo_filename)

    print(f"成功创建 {emo_filename}")


def json_to_xlsx(json_path, output_path=None):
    """将指定的JSON文件内容转换为XLSX文件"""
    
    # 如果没有提供输出路径，则默认使用JSON文件所在目录
    if not output_path:
        output_path = os.path.dirname(json_path)
    
    # 确保输出路径存在
    os.makedirs(output_path, exist_ok=True)
    
    # 构造输出文件路径
    output_file = os.path.join(output_path, 'output.xlsx')
    
    # 读取JSON文件
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    processed_data = []
    seen_files = set()
    
    for key, value in data.items():
        # 检查key是否包含中文字符
        if any('\u4e00' <= char <= '\u9fff' for char in key):
            continue
        
        # 获取文件名和扩展名
        filename = os.path.basename(value)
        name, ext = os.path.splitext(filename)
        
        # 只保留jpg和png格式的文件，并且检查是否重复
        if ext.lower() in ('.jpg', '.png') and filename not in seen_files:
            seen_files.add(filename)
            processed_data.append({
                'shortCut': f'i{key}',  # 在key前面加上字母i
                'meaning': name,        # 去除文件格式后的value
                'originalFile': filename  # 只保留文件名和格式
            })
    
    # 创建DataFrame并保存为Excel文件
    df = pd.DataFrame(processed_data)
    df.to_excel(output_file, index=False)
    print(f"成功创建 {output_file}")

import shutil

def copy_json_files(json_path, target_dir):
    """将JSON中的文件复制到指定目录"""
    
    # 确保目标目录存在
    os.makedirs(target_dir, exist_ok=True)
    
    # 读取JSON文件
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    seen_files = set()
    failed_copies = []

    for key, value in data.items():
        # 检查key是否包含中文字符
        if any('\u4e00' <= char <= '\u9fff' for char in key):
            continue
        
        # 获取文件名和扩展名
        filename = os.path.basename(value)
        name, ext = os.path.splitext(filename)
        
        # 只保留jpg和png格式的文件，并且检查是否重复
        if ext.lower() in ('.jpg', '.png') and filename not in seen_files:
            seen_files.add(filename)
            source_file = Path(value)
            
            try:
                if source_file.exists():
                    shutil.copy2(source_file, target_dir)
                else:
                    failed_copies.append(str(source_file))
            except Exception as e:
                failed_copies.append(str(source_file))
                print(f"拷贝失败: {source_file}, 错误信息: {e}")
    
    if failed_copies:
        print("以下文件拷贝失败:")
        for failed_copy in failed_copies:
            print(failed_copy)


if __name__ == '__main__':

    # 根据表格生成EmotionConfig.json文件
    dir_path = r'C:\Users\kan\Desktop\全部表情包'
    group_name = 'test'

    print("开始执行")
    # success_flag = manage_config_json(f'{dir_path}\\{group_name}', mode='new', strictness=2)
    success_flag = False
    if success_flag:
        # 从后往前查找最后一个反斜杠的索引
        last_backslash_index = dir_path.rfind('\\')

        # 如果找到了反斜杠
        if last_backslash_index != -1:
            # 使用切片分别获取路径的两部分
            part1 = dir_path[:last_backslash_index]  # 反斜杠之前的部分
            part2 = dir_path[last_backslash_index + 1:]  # 反斜杠之后的部分
            compress_to_emo(part1, part2, output_filename="CustomEmo")
    

    
    # 将handles.json转换为output.xlsx文件
    json_to_xlsx(r'D:\projects\auto_customer\config\hotstrings_cn.json')

    
    # 将handles.json中的文件复制到指定目录
    # copy_json_files('C:\\path\\to\\your\\file.json', 'C:\\path\\to\\target\\folder')