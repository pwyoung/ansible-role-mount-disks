#!/usr/bin/env python

import argparse


def main():
    disk_pattern = "Default Test Message in Python Script"

    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--disk-pattern',
                        action='store', type=str, dest="disk_pattern",
                        help='Pattern for finding disks to partition and mount',
                        default=disk_pattern)
    args = parser.parse_args()

    msg = "Python Script: Disk pattern is " + args.disk_pattern
    print( msg )
    os.system("ls / > /tmp/mount_disks.py.out")

if __name__ == "__main__":
    main()
