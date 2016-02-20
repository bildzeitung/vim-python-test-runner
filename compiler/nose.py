""" nose test runner
"""

import ast
import os
import re
import sys

from subprocess import PIPE, Popen
from tempfile import NamedTemporaryFile
from xml.dom.minidom import parse


def process_failure(name, txt):
    """ Process test failure items in XUnit output """
    regex = re.compile(r'\s*File "(.+)", line (\d+), in (.+)')
    regex2 = re.compile(r'^\S')

    message = None
    for line in txt.split('\n'):
        if not message:
            match = regex.match(line)
            if match:
                fname, line_no, method = match.groups()
                if method == name:
                    message = ':'.join([fname, line_no])
        else:
            match = regex2.match(line)
            if match:
                message += ':{0}'.format(line)
                return message

class Finder(ast.NodeVisitor):
    """ Visitor to get the line number of a specific function """
    def __init__(self, tofind):
        super(self.__class__, self).__init__()
        self.tofind = tofind
        self.lineno = None

    def visit_FunctionDef(self, fdef):
        """ Is the function a match? If so, memoize the line number """
        if fdef.name == self.tofind:
            self.lineno = fdef.lineno


def process_error(inname, name, txt):
    """ Process error items in XUnit output """
    regex = re.compile(r'\s*File "(.+)", line (\d+), in (.+)')
    regex2 = re.compile(r'^\S')

    message = None
    for line in txt.split('\n'):
        if not message:
            match = regex.match(line)
            if match:
                fname, line_no, method = match.groups()
                if method == name:
                    message = ':'.join([fname, line_no])
        else:
            match = regex2.match(line)
            if match:
                message += ':{0}'.format(line)
                return message

    # another form factor is (<filename>, <line>)
    # but for this, the basename is needed
    inbase = os.path.basename(inname)
    regex = re.compile(inbase + r', line (\d+)')
    match = regex.search(txt)
    if match:
        return ':'.join([inname, match.groups()[0], txt])

    # If this fires, then it's a more generic error with the test function
    tree = ast.parse(open(inname).read())
    finder = Finder(name)
    finder.visit(tree)

    results = ['pyerror:{0}:{1}'.format(inname, finder.lineno)]
    for line in txt.split('\n'):
        if line.strip():
            results.append('~' + line.strip())

    results.append('pyerrorend')
    return '\n'.join(results)


def process_xunit(inname, fname):
    """ Process the XUnit output file """
    doc = parse(fname)
    results = []

    for cases in doc.getElementsByTagName('testcase'):
        name = cases.getAttribute('name')
        for failure in cases.getElementsByTagName('failure'):
            message = failure.getAttribute('message')
            result = process_failure(name, message)
            if result:
                results.append(result)

        for error in cases.getElementsByTagName('error'):
            message = error.getAttribute('message')
            results.append(process_error(inname, name, message))

    #print doc.toprettyxml()

    return '\n'.join(results)


def main():
    """ Run nose, with options, and munge the XUnit ouput """
    tfile = NamedTemporaryFile(delete=False)
    args = ['nosetests', '--with-xunit', '--xunit-file={0}'.format(tfile.name)]
    args.extend(sys.argv[1:])

    #print 'RUNNING: %s' % args

    proc = Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    #stderr, stdout = proc.communicate()
    proc.communicate()

    #print 'STDERR: %s STDOUT: %s' % (stderr, stdout)
    #print '---'
    #print temp.name
    #print '---'
    print process_xunit(sys.argv[-1], tfile.name)

    os.unlink(tfile.name)

if __name__ == '__main__':
    main()

