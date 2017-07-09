#!/usr/bin/env python

import os
import re
import time
import datetime
import commands

git_dir = "HuiPython"


def main():
    global git_dir
    GIT_STAT_CMD = 'git log --stat'
    GIT_DETAILS_CMD = 'git log --stat'
    t = 3 * 60

    os.chdir(git_dir)

    d1 = datetime.datetime.now()
    dt = d1.strftime('%a %b %d')
    print "*************1"
    print dt

    i = 15
    d2 = d1 + datetime.timedelta(days=-i)
    print "*************6"
    print d2
    two = d2.strftime('%a %b')
    print "*************7"
    print two
    da = int(d2.strftime('%d'))
    print "*************8"
    print da
    two_weeks_day = '%s %s' % (two, da)
    print "*************2"
    print two_weeks_day
    twy = d2.strftime('%Y')
    print "*************3"
    print twy

    gp = commands.getoutput('git pull')
    log = commands.getoutput('git log')

    commit_one = re.search(r'commit\s(.*)', log).group(1)
    print "commit_one: ", commit_one
    commit_two = ''

    while True:
        content = r'commit\s(.*)\n.*\n.*%s\s.*\s%s\s' % (two_weeks_day, twy)
        print "****************content: ", content
        m = re.search(content, log)
        print "******m: ", m
        if m:
            commit_two = m.group(1)
            break
        else:
            i = i + 1
            d2 = d1 + datetime.timedelta(days=-i)
            two_weeks_day = d2.strftime('%a %b %d')
    print commit_one
    print commit_two

    cmd_stat = '%s %s...%s' % (GIT_STAT_CMD, commit_one, commit_two)
    cmd_detail = '%s %s...%s' % (GIT_DETAILS_CMD, commit_one, commit_two)
    result_stat = commands.getoutput(cmd_stat)
    result_detail = commands.getoutput(cmd_detail)

    print "*************4"
    print result_stat
    print "*************5"
    print result_detail


if __name__ == '__main__':
    main()
