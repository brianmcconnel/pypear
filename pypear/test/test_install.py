import os
import pathlib
from pypear.install import install, vimrc_prepend, gen_vimrc

from tempfile import TemporaryDirectory

import pytest

current_path = str(pathlib.Path(__file__).parent.absolute())
install_dir = str(pathlib.Path.home()) + '/.pypear'

@pytest.fixture()
def tmp_config_file():
    with TemporaryDirectory() as tmp_dir:
        file_name = tmp_dir + '/.vimrc'
        with open(file_name, 'w') as f:
            f.write('::::vimrc content:::::\n')
        yield file_name


def test_install():
    install()
    assert os.path.exists(install_dir)
    assert os.path.exists(install_dir + '/plugins/vim/')

def test_vimrc_prepend(tmp_config_file):
    tc = tmp_config_file
    vimrc_prepend(tc)
    with open(tc) as f:
        result = f.read()
    assert 'vimrc content' in result
    assert 'pypear\n::::vimrc' in result

