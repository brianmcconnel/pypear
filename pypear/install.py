from zipfile import ZipFile
import os
import pathlib
import shutil
import subprocess

current_path = str(pathlib.Path(__file__).parent.absolute())
install_dir = os.path.join(str(pathlib.Path.home()),  '.pypear')
vim_template = os.path.join(str(pathlib.Path.home()), '.pypear/vimrc')
vim_plugins_dir = os.path.join(install_dir, 'plugins/vim')
vimrc_template = os.path.join(current_path, 'vimrc_template')


def install():
    """Main installation entry point"""
    print('Installing pypear: Terminal based python development')
    print('Unpacking vim plugins...')
    with ZipFile(os.path.join(current_path,  'vim/plugins.zip')) as zip:
        if os.path.exists(install_dir):
            shutil.rmtree(install_dir)
        os.mkdir(install_dir)
        zip.extractall(path=install_dir)
        git_plugins()
        gen_vimrc()
        print('Pypear has finished installation in the ~/.pypear folder.')
        link_vimrc()


def vimrc_prepend(file_name):
    """Prepends the vimrc with pypear"""
    with open(file_name, 'r') as f:
        content = f.read()
    with open(file_name, 'w') as f:
        f.write('pypear\n')
        f.write(content)


def gen_vimrc():
    """Generates the pypear vimrc file"""
    with open(vim_template, 'w') as f:
        f.write('filetype off\n')
        f.write('set rtp+=~/.pypear/plugins/vim/Vundle.vim\n')
        f.write('call vundle#begin()\n')
        for filename in os.listdir(vim_plugins_dir):
            directory = os.path.join(vim_plugins_dir, filename)
            if os.path.isdir(directory):
                f.write("Plugin 'file://" + directory + "'\n")
        with open(vimrc_template) as vim:
            for line in vim:
                f.write(line)


def git_init(directory):
    """Runs the git command to initialize the plugin folder as a git repo"""
    return subprocess.Popen(["git", "init"], cwd=directory)


def git_add(directory):
    """Runs the git command to add all the files for the plugin"""
    return subprocess.Popen(["git", "add", "*"], cwd=directory)


def git_commit(directory):
    """Runs the git command to commit everything in a given directory"""
    return subprocess.Popen(["git", "commit", "--all", "-m", "pypear init"], cwd=directory)


def git_plugins():
    """Runs an initialization of the vim plugins to make them work with vundle"""
    for filename in os.listdir(vim_plugins_dir):
        directory = os.path.join(vim_plugins_dir, filename)
        if os.path.isdir(directory):
            git_init(directory).wait()
            git_add(directory).wait()
            git_commit(directory).wait()


def backup_vimrc():
    """Makes a backup of the current vimrc to .vimrc.bak"""
    print("Backing up current .vimrc to vimrc.bak just in case...")
    vim_file = os.path.join(str(pathlib.Path.home()),  '.vimrc')
    vim_backup = os.path.join(str(pathlib.Path.home()),  '.vimrc.bak')
    return subprocess.Popen(["mv", vim_file, vim_backup])


def link_vimrc():
    """Automatically link pypear vimrc"""
    print('The file at the following location can be used to as .vimrc:', vim_template)
    print('Note: for a simple install create a symbolic link: ln -s %s ~/.vimrc' % vim_template)
    if input('Would you like pypear to do this automatically? (y/n): ') == 'y':
        backup_vimrc().wait()
        vim_file = os.path.join(str(pathlib.Path.home()),  '.vimrc')
        subprocess.Popen(["ln", "-s", vim_template, vim_file]).wait()
