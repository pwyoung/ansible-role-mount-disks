#!/usr/bin/env python

import argparse
import os

def main():
    disk_pattern = "/dev/nvme_default"

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--disk-pattern',
                        action='store', type=str, dest="disk_pattern",
                        help='Pattern for finding disks to partition and mount',
                        default=disk_pattern)
    args = parser.parse_args()

    msg = "Python Script: Disk pattern is " + args.disk_pattern
    print( msg )
    os.system("echo `hostname` `whoami` > /tmp/mount_disks.py.out")

if __name__ == "__main__":
    main()
