#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Gordon Mathurin"

import sys
import logging
import signal
import time
import argparse
import os

exit_flag = False


def search_for_magic(filename, start_line, magic_string):
    # Your code here
    return


def watch_directory(path, magic_string, extension, interval):
    # Your code here
    return


def create_parser():
    # Your code here
    parser = argparse.ArgumentParser(
        description="Watch for specfic word to be added")
    parser.add_argument(
        '--topoll', help='controls polling interval', action='')
    parser.add_argument('--tosearch',
                        help='search for magic word', action='')
    parser.add_argument(
        '--tofilter',
        help='filters what kind of file extenion to search within', action='')
    parser.add_argument(
        '--todir', help='specifies the directory to watch', action='')
    return parser
    return


def signal_handler(sig_num, frame):
    # Your code here
    # log the associated signal name
    logger.warn('Received ' + signal.Signals(sig_num).name)
    return


def main(args):
    # Your code here
    parser = create_parser()
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)
    return

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    # Now my signal_handler will get called if OS sends
    # either of these to my process.

    while not exit_flag:
        try:
            # call my directory watching function
            pass
        except Exception as e:
            # This is an UNHANDLED exception
            # Log an ERROR level message here
            pass

        # put a sleep inside my while loop so I don't peg the cpu usage at 100%
        time.sleep(polling_interval)


if __name__ == '__main__':
    main(sys.argv[1:])
