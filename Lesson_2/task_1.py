import re
import csv

import chardet
import numpy as np

from settings import (
    TEST_FILE_DIR,
    get_files,
)


def get_data() -> list:
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [os_prod_list, os_name_list, os_code_list, os_type_list]
    headers = [
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы'
    ]
    prod_pattern = re.compile(r'Изготовитель системы:\s*\S*')
    name_pattern = re.compile(r'Название ОС:\s*\S*')
    code_pattern = re.compile(r'Код продукта:\s*\S*')
    type_pattern = re.compile(r'Тип системы:\s*\S*')

    for file in get_files(TEST_FILE_DIR, '.txt'):
        with open(TEST_FILE_DIR.joinpath(file), 'rb') as f_obj:
            content = f_obj.read()
            encoding_params = chardet.detect(content)
            decode_cont = content.decode(encoding_params['encoding'])

        os_prod_list.append(prod_pattern.findall(decode_cont)[0].split()[2])
        os_name_list.append(name_pattern.findall(decode_cont)[0].split()[2])
        os_code_list.append(code_pattern.findall(decode_cont)[0].split()[2])
        os_type_list.append(type_pattern.findall(decode_cont)[0].split()[2])

    main_data = np.array(main_data, dtype=object).T.tolist()
    main_data.insert(0, headers)
    return main_data


def write_to_csv(data: list) -> None:
    with open(TEST_FILE_DIR.joinpath('task_1_result.csv'), 'w', encoding='utf-8') as f_obj:
        writer = csv.writer(f_obj)
        for line in data:
            writer.writerow(line)


if __name__ == '__main__':
    write_to_csv(get_data())
