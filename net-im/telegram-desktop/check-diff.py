#!/usr/bin/env python

import subprocess

def get_modified_files():
    output = subprocess.check_output("git status -s", shell=True)
    for line in output.split('\n'):
        line = line.strip()
        if not line.startswith('M'):
            continue
        yield line.split(' ', 1)[1]


def diff_only_in_time(filename):
    output = subprocess.check_output("git diff %s" % filename, shell=True)
    for line in output.split('\n'):
        line = line.rstrip()
        if not line.startswith('+') and not line.startswith('-'):
            continue
        if line.startswith('----') or line.startswith('+---'):
            continue
        if line.startswith('---') or line.startswith('+++'):
            continue
        return False
    return True


def git_revert(filename):
    print("revert %s" % filename)
    subprocess.check_call("git checkout %s" % filename, shell=True)


for filename in get_modified_files():
    if diff_only_in_time(filename):
        git_revert(filename)
