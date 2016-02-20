# vim-python-test-runner.vim

A simple way of running tests for your python files from within VIM.

This plugin was created to allow running your regular python unit tests with
nosetests.

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/JarrodCTaylor/vim-python-test-runner ~/.vim/bundle/vim-python-test-runner`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Plugin 'JarrodCTaylor/vim-python-test-runner'` to .vimrc
  - Run `:PluginInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/JarrodCTaylor/vim-python-test-runner'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/JarrodCTaylor/vim-python-test-runner'` to .vimrc
  - Run `:PlugInstall`

## Requirements

You need a VIM version that was compiled with python support, which is typical
for most distributions on Linux/Mac.  You can check this by running
``vim --version | grep +python``
if you get a hit you are in business.

Tests are ran with nosetest so that will need to be
pip installed in order for the plugin to function properly.

## Usage

The plugin provides nine commands:

- `NosetestFile`: Run all tests for the current file
- `NosetestClass`: Run all tests in the current class
- `NosetestMethod`: Run the current test method (inside of a class)
- `NosetestBaseMethod`: Run the current test method (outside of a class)
- `RerunLastTests`: Rerun the last tests

All arguments can be tab-completed. Ensure that your cursor is within a
file, class or method as appropriate for the command being called.

For ease of usage you can map the above actions to a shortcut. For example,
if you wanted leader mappings you could set something like the following in
your vimrc:

```
    nnoremap <Leader>nf :NosetestFile<CR>
    nnoremap <Leader>nc :NosetestClass<CR>
    nnoremap <Leader>nm :NosetestMethod<CR>
    nnoremap <Leader>nb :NosetestBaseMethod<CR>
    nnoremap <Leader>rr :RerunLastTests<CR>
```

### Quickfix Results

Your tests results will be available in the quickfix window after they finish
running and you return to your Vim buffer. Open quickfix with `:copen` and
you can jump to failing tests by placing your cursor on the desired test and
pressing enter.

