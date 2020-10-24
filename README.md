# :pie::pear:pypear: Terminal based python development.
![BUILD](https://github.com/brianmcconnel/pypear/workflows/build/badge.svg)

Motivation:  How does a python developer streamline test driven development with only an ssh connection?

Installation: Caution this is a work in progress. The following command will install the vim plugins under the ~/.pypear/plugins/vim/ folder.
```
pip install pypear
pypear #installs plugins in the ~/.pypear folder
```

There are many great tools available for python development.  This set of tools was collected to streamline test driven development through just a terminal and a simple pip install. (Future: Would like to have this available from conda-forge)

Visual Studio Code Remote Development plugins are excellent and are likely to be a better choice in most cases.  However, the simplicity of workflow possible with this collection of tools is impressive and should not be overlooked.  As with any tool it comes at the cost of learning to use the tools properly.

## Terminal Multiplexing / Session Management / Pair Programming Support
tmux: Terminal multiplexer running on server size, supports pair programming and session suspension.

## Text Editing
vim (or Neovim): Vim is everywhere and is very usable over connections of any speed. Vim8 is recommended. Neovim because I like it. :)<br>
Vundle: vim plugin manager (just because it works)<br>

## Version Control
git: the only way to configuration manage code.<br>
vim-fugitive: vim git plugin so good it should be illegal<br>
vim-gitgutter: vim git gutter plugin<br>
nerdtree: vim enhanced file explorer plugin<br>
nerdtree-git-plugin: vim git enhancement for file explorer plugin<br>
pre-commit: framework for managing hooks for pre-commit actions<br>
pre-commit-hooks: commonly used pre-commit hooks<br>

## Linting
ale: vim code linting for many languages plugin<br>
flake8: python linting<br>
autopep8: automatic pep8 formating (pre-commit linting)<br>

## Searching
ctags: enables simple navigation of large or small code bases within vim.<br>
ctrlp: fuzzy file search (interested in better alternatives)<br>

## Testing
pytest: the "best" python testing framework.<br>
pytest-vim-compiler: pytest compiler<br>
vim-dispatch: enables asyc test and command running with tmux<br>

## Themes (Because it should be attractive)
vim-airline: Vim theme<br>
vim-airline-themes: airline themes<br>
tumxline: Coordinates tmux theme with vim theme<br>
promptline: Coordinates prompt theme with vim theme<br>

## Cheat Sheets
tmux:<br>
vim:<br>

## TODO
1. Add good cheatsheet links
2. Build autodocs based on plugin documentation
3. conda-forage installation
4. neovim conda-forge installation
5. pypear vim documentation
6. offline pre-commit configuration

## Contribution
I don't intend to put a lot of effort into this packages, but completely willing to collaborate with others. If anyone knows of a better meta package that I could support rather than rolling my own let me know.

## License
MIT

All plugins retain existing licences:  Vim, MIT, Apache 2.0, Public Domain (WTFPL)

