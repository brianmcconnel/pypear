# :pie::pear:pypear: Adequate terminal based python development.
![BUILD](https://github.com/brianmcconnel/pypear/workflows/CI/badge.svg)

Motivation:  How does a python developer streamline test driven development with only an ssh connection?

To install run the following command.
```
pypear
```

There are many great tools available for python development.  This set of tools was collected to streamline test driven development through just a terminal and a simple conda install from conda-forge.

Visual Studio Code Remote Development plugins are excellent and are likely to be a better choice in most cases.  However, the simplicity of workflow possible with this collection of tools is impressive and should not be overlooked.  As with any tool it comes at the cost of learning to use the tools properly.

General arrangement, package installs development tools (git, tmux, vim, flake8, autopep8, ctags, pytest) and vim plugins will be distributed with the package (location tbd).

## Terminal Multiplexing / Session Management / Pair Programming Support
tmux: Terminal multiplexer running on server size, supports pair programming and session suspension.

## Text Editing
vim (or Neovim): Vim is everywhere and is very usable over connections of any speed. Vim8 is recommended. Neovim because I like it. :)
Vundle: vim plugin manager (just because it works)

## Version Control
git: the only way to configuration manage code.
vim-fugitive: vim git plugin so good it should be illegal
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

## TODO
1. Add good cheatsheet links
2. Build autodocs based on plugin documentation

## Contribution
I don't intend to put a lot of effort into this packages, but completely willing to collaborate with others. If anyone knows of a better meta package that I could support rather than rolling my own let me know.

## License
MIT

All plugins retain existing licences:  Vim, MIT, Apache 2.0, Public Domain (WTFPL)

