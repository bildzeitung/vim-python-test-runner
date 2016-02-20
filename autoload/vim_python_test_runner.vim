
if !has('python')
    finish
endif

" -----------------------------
" Add our directory to the path
" -----------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

function! vim_python_test_runner#RunDesiredTests(command_to_run)
python << endPython
import os
from sys import platform as _platform

"""
def get_proper_command(desired_command, current_directory):
    current_line_index = vim.current.window.cursor[0]
    FUNCTIONS = {
        "nose_file": lambda: get_command_to_run_current_file_with_nosetests(vim.current.buffer.name),
        "nose_class": lambda: get_command_to_run_current_class_with_nosetests(vim.current.buffer.name, current_line_index, vim.current.buffer),
        "nose_method": lambda: get_command_to_run_current_method_with_nosetests(vim.current.buffer.name, current_line_index, vim.current.buffer),
        "nose_base_method": lambda: get_command_to_run_current_base_method_with_nosetests(vim.current.buffer.name, current_line_index, vim.current.buffer),
        "rerun": lambda: get_command_to_rerun_last_tests()
    }
    return FUNCTIONS[desired_command]()

def run_desired_command_for_os(command_to_run):
    if "nose" in vim.eval("a:command_to_run") or "nose" in command_to_run:
        vim.command("{0} 2>&1 | tee /tmp/test_results.txt".format(command_to_run))
    elif _platform in ('linux', 'linux2', 'darwin'):
        raise Exception('unsupported')
"""

def main():
    current_directory = vim.current.buffer.name
    #try:
    #    command_to_run = get_proper_command(vim.eval("a:command_to_run"), current_directory)
    #except Exception as e:
    #    print(e)
    #run_desired_command_for_os(command_to_run)
    vim.command('silent make! {0} | cw'.format(current_directory))
    vim.command('redraw!')

vim.command('wall')
main()
endPython
endfunction

