"""Demo of argparse command-line argument.
"""
import argparse


def main():
    args = cmdline_parser()
    print('run_date = ', args.run_date)


def cmdline_parser():
    parser = argparse.ArgumentParser(
        description='Description of script for help display'
    )
    parser.add_argument(
        'run_date',
        help='run date to process results from'
    )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
