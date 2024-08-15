import os
import re
import chardet
import shutil

def replace_chars_in_ini_files(root_dir, char_mapping):
    
    # 遍历目录树
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.ini'):
                file_path = os.path.join(root, file)
                shutil.copyfile(file_path, os.path.join(root, 'DISABLED' + file))
                with open(file_path, 'rb') as f:
                    raw_data = f.read()
                    result = chardet.detect(raw_data)
                    encoding = result['encoding']

                with open(file_path, 'r', encoding=encoding) as file:
                    content = file.read()
                # 替换字符
                
                for old, new in char_mapping.items():
                    content = re.sub('hash = ' + old.lower(), 'hash = ' + new.lower(), content)
                with open(file_path, 'w', encoding=encoding) as file:
                    file.write(content)


char_mapping = {
                #长离
                '77975500':'5f8aac45', 

                'D8DECBCA':'1CCB8008', 
                'FD9483CA':'060F5303', 
                '8f067708':'f23483e3',
                #吟霖
                '86b95122':'00120eee',
                '148a83c6':'33d00a20',
                '750390fa':'584b7755',
                '9ebf7cad':'065eae3',
                #白芷
                '37bed36b': '718456ac',
                '52c9b804': 'd7756134',

                #维里奈
                '83ced9f7':'82aa82e1',
}
print(char_mapping)

# 指定要搜索的目录
root_dir = '.'
replace_chars_in_ini_files(root_dir, char_mapping)


