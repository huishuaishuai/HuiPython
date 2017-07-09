#!/usr/bin/env python

import os
import re
import time
import commands

git_dir = "HuiPython"


def main():
    global git_dir
    t = 5 * 60

    t1 = time.time()
    t2 = time.time() - t

    d1 = time.asctime(time.localtime(t1))
    print d1
    print "%s %s" % (d1.split("  ")[0], d1.split("  ")[1])
    d2 = time.asctime(time.localtime(t2))
    print d2

    print "Sat Jul 8 18:46:40 2017"



    # os.chdir(git_dir)
    #
    # gp = commands.getoutput('git pull')
    # log = commands.getoutput('git log')
    # print log
    #
    # commit_one = re.search(r'commit\s(.*)', log).group(1)
    # print commit_one


if __name__ == '__main__':
    main()
