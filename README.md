# :pie::pear:pypear: Adequate terminal based python development.

Motivation:  How does a python developer streamline test driven development with only an ssh connection?

There are many great tools available for python development.  This set of tools were collected to streamline test driven development through just a terminal and a simple conda install from conda-forge.

Visual Studio Code Remote Development plugins are excellent and are likely to be a better choice in most cases.  However, the simplicity of workflow possible with this collection of tools is impressive and should not be overlooked.  As with any tool it comes at the cost of learning to use the tools properly.

## Terminal Multiplexing / Session Management / Pair Programming Support
tmux: Terminal multiplexer running on server size, supports pair programming and session suspension.

## Text Editing
vim (or Neovim): Vim is everywhere and is very usable over connections of any speed. Neovim because I like it. :)
Vundle: vim plugin manager (just because it works)

## Version Control
git: the only way to configuration manage code.
vim-fugitive: vim git plugin
vim-gitgutter: vim git gutter plugin
nerdtree: vim enhanced file explorer plugin
nerdtree-git-plugin: vim git enhancement for file explorer plugin
pre-commit: framework for managing hooks for pre-commit actions
pre-commit-hooks: commonly used pre-commit hooks

## Linting
ale: vim code linting for many languages plugin
flake8: python linting
autopep8: automatic pep8 formating (pre-commit linting)

## Searching
ctags: enables simple navigation of large or small code bases within vim.
ctrlp: fuzzy file search (interested in better alternatives)

## Testing
pytest: the "best" python testing framework.
pytest-vim-compiler: pytest compiler
vim-dispatch: enables asyc test and command running with tmux

## Themes (Because it should be attractive)
vim-airline: Vim theme
vim-airline-themes: airline themes
tumxline: Coordinates tmux theme with vim theme
promptline: Coordinates prompt theme with vim theme

## Cheat Sheets
tmux:
vim:

## License

MIT

All plugins retain existing licences:  Vim, MIT, Apache 2.0, Public Domain (WTFPL)

