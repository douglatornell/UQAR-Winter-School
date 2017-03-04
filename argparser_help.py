"""Demo of argparse command-line help.
"""
import argparse


def main():
    args = cmdline_parser()


def cmdline_parser():
    parser = argparse.ArgumentParser(
        description='Description of script for help display'
    )
    args = parser.parse_args()


if __name__ == '__main__':
    main()
