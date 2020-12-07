#!/usr/bin/env python

import argparse


def main():
    test_msg = "Default Test Message in Python Script"
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--test-message',
                        action='store', type=str, dest="test_msg",
                        help='Test Message',
                        default=test_msg)
    args = parser.parse_args()

    print("Test message is: " + args.test_msg)

if __name__ == "__main__":
    main()
