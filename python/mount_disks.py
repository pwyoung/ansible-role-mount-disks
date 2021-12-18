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

    print("Disk pattern is: " + args.disk_pattern)

if __name__ == "__main__":
    main()
