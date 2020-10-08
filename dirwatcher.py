#!/usr/bin/env python3
"""
Dirwatcher - A long-running program
"""

__author__ = "Gordon Mathurin"

import argparse
import sys
import os
import logging
import signal
import datetime
# import time

exit_flag = False
start_time = ''
master_dict = {}
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s,%(message)s')
logger = logging.getLogger(__name__)


def create_dir(ns):
    """ Checks if directory exists, return true or false"""
    error_message = 'Creation of directory failed or directory already exists'
    if os.path.isdir(ns.todir):
        return True
    else:
        return False


# def scan_single_file(filename):
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.info)
#     logger.error('')

#     pass

def signal_handler(sig_num, frame):
    # Your code here
    """Signal event handler setup"""
    global exit_flag
    global start_time
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.WARNING)
    logger.warning('Received ' + signal.Signals(sig_num).name)
    logger2 = logging.getLogger(__name__)
    logger2.setLevel(logging.INFO)
    logger2.info(
        f"""
        -----------------------------------------------------
        \tStopped {sys.argv[0]}
        \tUptime was: {datetime.datetime.now() - start_time}
        -----------------------------------------------------
       """
    )
    exit_flag = True


def watch_directory(ns):
    # Your code here
    temp_dict = {}
    check_dir_status = create_dir(ns.todir)

    try:
        if check_dir_status:
            for content in os.walk(ns.todir):
                files = content[2]
            for file in files:
                if file.endswith(ns.tofilter):
                    temp_dict.setdefault(file, [])
        else:
            logger.error(f"{ns.todir} doesn't exists")
    except Exception as e:
        logger.exception(f'{e}')


def compare_dict(temp_dict, ns):
    """ Compares files between mast dict and temp dict"""
    try:
        for file in temp_dict:
            if file not in master_dict:
                logger.info(f'{file} was added to {ns.todir}')
                master_dict[file] = []
        for file in master_dict:
            if file not in temp_dict:
                logger.info(f'{file} was deleted from {ns.todir}')
                del master_dict[file]
    except Exception as e:
        logger.exception(f'{e}')


def search_for_magic(ns):
    # Your code here
    """Search for magic word through file"""
    try:
        for file in master_dict:
            with open(f'{ns.todir}/{file}') as f:
                for i, line in enumerate(f):
                    if ns.magic in line:
                        if i not in master_dict[file]:
                            master_dict[file].append(i)
                            logger.info(
                                f'Magic Word: {file} on line {i+1}')
    except Exception as e:
        logger.exception(f'{e}')


def create_parser():
    # Your code here
    parser = argparse.ArgumentParser(
        description="Watch for specfic word to be added")
    parser.add_argument(
        '--interval', help='controls polling interval',
        type=int, default=1)
    parser.add_argument('magic',
                        help='magic string to look for')
    parser.add_argument(
        '--tofilter',
        help='filters what kind of file extenion to search within',
        default='.txt')
    parser.add_argument(
        'todir', help='specifies the directory to watch')
    return parser


def main(args):
    # Your code here
    parser = create_parser()
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        sys.exit(1)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    while not exit_flag:
        try:
            # call my directory watching function
            watch_directory(ns)
            compare_dict(ns)
            search_for_magic(ns)
        except Exception as e:
            logger.exception(f'{e}')

        # put a sleep inside my while loop so I don't peg the
        #  cpu usage at 100%
        # time.sleep(polling_interval)


if __name__ == '__main__':
    main(sys.argv[1:])
