#!/usr/bin/env python2

import subprocess
import os
import glob

def git_get_modified_files():
    output = subprocess.check_output("git status -s", shell=True)
    for line in output.split('\n'):
        line = line.strip()
        if not line.startswith('M'):
            continue
        yield line.split(' ', 1)[1]


def git_diff_content(filename):
    output = subprocess.check_output("git diff %s" % filename, shell=True)
    return output.split('\n')


def diff_only_in_time(lines):
    for line in lines:
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


def ports_get_modified_files():
    for oldfilepath in glob.glob("/usr/ports/net-im/telegram-desktop/files/*"):
        oldfilename = os.path.basename(oldfilepath)
        newfilepath = os.path.join("files", oldfilename)
        if not os.path.exists(newfilepath):
            continue
        oldcontent = open(oldfilepath).read()
        newcontent = open(newfilepath).read()
        if oldcontent != newcontent:
            yield newfilepath


def ports_diff_content(filename):
    try:
        output = subprocess.check_output("diff -ruN %s %s" %
                                         (os.path.join("/usr/ports/net-im/telegram-desktop",
                                                       filename), filename), shell=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    return output.split('\n')


def ports_revert(filename):
    print("revert %s" % filename)
    subprocess.check_call("cp %s %s" % (os.path.join("/usr/ports/net-im/telegram-desktop",
                                                   filename), filename), shell=True)


def check_git_diff():
    for filename in git_get_modified_files():
        diff_content = git_diff_content(filename)
        if diff_only_in_time(diff_content):
            git_revert(filename)


def check_ports_diff():
    for filename in ports_get_modified_files():
        diff_content = ports_diff_content(filename)
        if diff_content == []:
            print("no diff: %s" % filename)
            continue

        if diff_only_in_time(diff_content):
            ports_revert(filename)
            print('\n'.join(diff_content))


check_ports_diff()
