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

master_dict = {}

# check if directory exists, if exist use os.walk() and look at file --> can be its a own function
# might want to have 2 dicts master and temp(temp inside function)
# maybe add files as keys in temp dict
# compare temp to master to see if added into master

# use try except logic for both functions


def create_dir(path):
    """ Checks if directory exists, if not create it """
    if not os.path.isdir(path):
        try:
            os.makedirs(path)
        except OSError:
            logging.info(f'Creation of dir {path} failed')
            return False
    return True


def watch_directory(path, magic_string, extension, interval):
    # Your code here
    # temp_dict = {}

    check_dir_status = create_dir(path)
    signal.signal(signal.SIGINT, signal_handler)

    if not check_dir_status:
        return

    while
    try:
        pass
    except Exception as e:
        pass

    return


def signal_handler(sig_num, frame):
    # Your code here
    # log the associated signal name
    logging.warn('Received ' + signal.Signals(sig_num).name)
    return


def search_for_magic(filename, start_line, magic_string):
    # Your code here
    # use master dict to check for magic dict

    try:
        pass
    except Exception as e:
        pass
    return


def create_parser():
    # Your code here
    parser = argparse.ArgumentParser(
        description="Watch for specfic word to be added")
    parser.add_argument(
        '--interval', help='controls polling interval',
        type=int, default=3)
    parser.add_argument('--magic',
                        help='magic string to look for')
    parser.add_argument(
        '--tofilter',
        help='filters what kind of file extenion to search within')
    parser.add_argument(
        '--todir', help='specifies the directory to watch')
    return parser


def main(args):
    # Your code here
    parser = create_parser()

    if not ns:
        parser.print_usage()
        sys.exit(1)

    ns = parser.parse_args(args)

    ext = ns.tofilter
    polling_interval = ns.interval
    magic_string = ns.magic
    directory_watch = ns.todir

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
