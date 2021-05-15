import os
import shutil


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def delete_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)


def create_file(file_path):
    open(file_path, 'w')


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)


def read_file(file_path) -> str:
    with open(file_path, 'r', encoding='utf8') as my_file:
        return my_file.read()


def is_file_exist(file_path):
    return os.path.exists(file_path)
