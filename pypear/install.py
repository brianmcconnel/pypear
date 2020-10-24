from zipfile import ZipFile
import os
import pathlib
import shutil

current_path = str(pathlib.Path(__file__).parent.absolute())
install_dir = os.path.join(str(pathlib.Path.home()),  '.pypear')
vim_template = os.path.join(str(pathlib.Path.home()), '.pypear/vimrc')
vim_plugins_dir = os.path.join(install_dir, 'plugins/vim')
vimrc_template = os.path.join(current_path, 'vimrc_template')


def install():
    print('Installing pypear: Terminal based python development')
    print('Unpacking vim plugins...')
    with ZipFile(os.path.join(current_path,  'vim/plugins.zip')) as zip:
        if os.path.exists(install_dir):
            shutil.rmtree(install_dir)
        os.mkdir(install_dir)
        zip.extractall(path=install_dir)
        gen_vimrc()
        print('Pypear has finished installation in the ~/.pypear folder.')
        print('The file at the following location can be used to as .vimrc:', vim_template)
        print('Note: for a simple install create a symbolic link: ln -s %s ~/.vimrc' % vim_template)


def vimrc_prepend(file_name):
    with open(file_name, 'r') as f:
        content = f.read()
    with open(file_name, 'w') as f:
        f.write('pypear\n')
        f.write(content)


def gen_vimrc():
    with open(vim_template, 'w') as f:
        f.write('filetype off\n')
        f.write('set rtp+=~/.pypear/plugins/vim/Vundle.vim\n')
        f.write('call vundle#begin()\n')
        for filename in os.listdir(vim_plugins_dir):
            directory = os.path.join(vim_plugins_dir, filename)
            if os.path.isdir(os.path.join(vim_plugins_dir, filename)):
                f.write("Plugin 'file://" + directory + "'\n")
        with open(vimrc_template) as vim:
            for line in vim:
                f.write(line)
