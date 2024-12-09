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
    """管理config.json文件"""

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

def json_to_xlsx(output_path='output.xlsx'):
    """将config.json保存为xlsx文件"""

    # json_path默认为当前目录下的文件
    json_path = os.path.join(os.getcwd(), 'EmotionConfig.json')  # 使用完整路径

    # 判断json_path是否存在
    if not os.path.exists(json_path):
        print(f"文件 {json_path} 不存在")
        return None
    
    # 读取JSON文件内容
    with open(json_path, 'r') as file:
        data = json.load(file)
    
    df = pd.DataFrame(data)
    df.to_excel(output_path, index=False)


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


dir_path = r'C:\Users\kan\Desktop\全部表情包'
group_name = 'test'

print("开始执行")
success_flag = manage_config_json(f'{dir_path}\\{group_name}', mode='new', strictness=2)
if success_flag:
    # 从后往前查找最后一个反斜杠的索引
    last_backslash_index = dir_path.rfind('\\')

    # 如果找到了反斜杠
    if last_backslash_index != -1:
        # 使用切片分别获取路径的两部分
        part1 = dir_path[:last_backslash_index]  # 反斜杠之前的部分
        part2 = dir_path[last_backslash_index + 1:]  # 反斜杠之后的部分
        compress_to_emo(part1, part2, output_filename="CustomEmo")