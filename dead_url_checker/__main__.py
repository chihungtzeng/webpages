# -*- coding: utf-8 -*-
"""
Check dead URLs.
"""
import argparse
import logging
import sys
from dead_url_checker import DeadURLChecker


def main():
    """
    Program entry.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    args = parser.parse_args()
    checker = DeadURLChecker(args.url)
    checker.run()


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)-15s %(message)s",
                        level=logging.INFO)
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
