#!/usr/bin/env python

import sys
import subprocess
import time


def get_uptime():

    # get boot time
    sp = subprocess.Popen(["sysctl", "-a"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = sp.communicate()

    if sp.returncode:
        print "-1"
        sys.exit(1)

    target = None
    for line in out.split("\n"):
        if line.find("kern.boottime") >= 0:
            target = line
            break

    if not target:
        print "-1"
        sys.exit(1)

    left = target.find(" sec = ") + len(" sec = ")
    right = target.find(",")

    boot_time = int(target[left:right])


    # current epoch
    current_epoch = int(time.time())

    print current_epoch - boot_time
    sys.exit(0)


if __name__ == "__main__":

    try:
        get_uptime()
    except Exception as e:
        print "-1"
        sys.exit(1)
