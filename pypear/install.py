from zipfile import ZipFile
import os
import pathlib
import subprocess
from argparse import ArgumentParser

current_path = str(pathlib.Path(__file__).parent.absolute())
install_dir = os.path.join(str(pathlib.Path.home()),  '.pypear')
vim_template = os.path.join(str(pathlib.Path.home()), '.pypear/vimrc')
vim_plugins_dir = os.path.join(install_dir, 'plugins/vim')
vimrc_template = os.path.join(current_path, 'vimrc_template')
parser = ArgumentParser()
parser.add_argument('-v', '--vimrc', action='store_true', help='backup current vimrc link to pypear vimrc.')


def parse_args():
    return parser.parse_args()


def install():
    """Main installation entry point"""
    print('Installing pypear: Terminal based python development')
    print('Unpacking vim plugins...')
    args = parse_args()
    with ZipFile(os.path.join(current_path,  'vim/plugins.zip')) as zip:
        if os.path.exists(install_dir):
            for rootdir, subdirs, filenames in os.walk(f"{install_dir}/"):
                for fn in filenames:
                    os.remove(os.path.join(rootdir, fn))
        else:
            os.mkdir(install_dir)
        zip.extractall(path=install_dir)
    print('Initializing git repos for plugins...')
    git_plugins()
    print('Generating a vimrc...')
    gen_vimrc()
    print('The file at the following location can be used to as .vimrc:', vim_template)
    print('Note: for a simple install create a symbolic link: ln -s %s ~/.vimrc' % vim_template)
    print('Pypear has finished installation in the ~/.pypear folder.')
    if args.vimrc:
        link_vimrc()
    install_plugins()
    print('Installation complete...')


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
    backup_vimrc().wait()
    print("Making a symbolic link to pypear vimrc...")
    vim_file = os.path.join(str(pathlib.Path.home()),  '.vimrc')
    subprocess.Popen(["ln", "-s", vim_template, vim_file]).wait()


def install_plugins():
    """Check for existing plugins and removed if they exist..."""
    vim_plugins = os.path.join(str(pathlib.Path.home()),  '.vim', 'bundle', )
    print("Removing existing bundles...")
    subprocess.Popen(['rm', '-rf', vim_plugins]).wait()
    print("Installing plugins...")
    subprocess.Popen(['vim', '-c', ':PluginInstall', '-c', 'x', '-c', 'x']).wait()
