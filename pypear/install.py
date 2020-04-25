from zipfile import ZipFile
import os
import pathlib
import shutil

current_path = str(pathlib.Path(__file__).parent.absolute())
install_dir = str(pathlib.Path.home()) + '/.pypear'
vim_template = str(pathlib.Path.home()) + '/.pypear/plugins/vimrc'


def install():
    with ZipFile(current_path + '/vim/plugins.zip') as zip:
        if os.path.exists(install_dir):
            shutil.rmtree(install_dir)
        os.mkdir(install_dir)
        zip.extractall(path=install_dir)


def vimrc_prepend(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    with open(file_name, 'w') as f:
        f.write('pypear\n')
        f.write(content)


def gen_vimrc():
    with open(vim_template) as f:
        result = f.read()
    return result
