#!/usr/bin/env python

import os
import re
import time
import commands

git_dir = "HuiPython"
git_url = "https://github.com/huishuaishuai/HuiPython.git"
branch = "dev"


def main():
    global git_dir
    t = 3 * 60

    os.chdir(git_dir)
    log = commands.getoutput('git log')
    commit_one = re.search(r'commit\s(.*)', log).group(1)
    print commit_one

    cmd = "git ls-remote %s %s" % (git_url, branch)
    a = commands.getoutput(cmd)
    print a[:40]
    if commit_one != a[:40]:
        commands.getoutput('git pull')
        print True
    else:
        print False

    q = commands.getoutput("ls -a")
    print q
    aa = re.search(r'READNE.md\s(.*)', q)
    print aa


if __name__ == '__main__':
    main()