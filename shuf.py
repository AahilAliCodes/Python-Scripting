#!/usr/bin/env python3
import argparse
import random
import sys


def get_input(args):

    if args.input_range:
        arguments = args.input_range.split("-")
        start = int(arguments[0])
        end = int(arguments[1])
        input_data = []
        for i in range(start, end + 1):
            input_data.append(i)
    elif args.echo:
        input_data = args.echo
    else:
        with open(args.file) if args.file != '-' else sys.stdin as f:
            input_data = f.readlines()

    return input_data


def main():
    parser = argparse.ArgumentParser(description="Randomly permute lines or values from a file or range of integers")
    parser.add_argument("-e", "--echo", nargs='+', help="Treat each ARG as an input line")
    parser.add_argument("-i", "--input-range", dest="input_range",
                        help="Treat each number LO through HI as an input line")
    parser.add_argument("-n", "--head-count", type=int, help="Output at most COUNT lines")
    parser.add_argument("-r", "--repeat", action="store_true", help="Output lines can be repeated")
    parser.add_argument("file", nargs='?', default='-', help="Input file name (use - for standard input)")

    args = parser.parse_args()

    count = None
    if args.head_count:
        count = int(args.head_count)
    input_data = get_input(args)

    printExtraLines = False
    if args.input_range or args.echo:
        printExtraLines = True

    if args.repeat and args.head_count:
        # Repeat n times if both options are present
        for i in range(args.head_count):
            for line in input_data:
                sys.stdout.write(str(line))
                if printExtraLines:
                    sys.stdout.write("\n")
    elif args.repeat:
        # Repeat indefinitely if only -r option is present
        while True:
            for line in input_data:
                sys.stdout.write(str(line))
                if printExtraLines:
                    sys.stdout.write("\n")
    elif count is not None:
        counter = 0
        while counter < count and counter < len(input_data):
            sys.stdout.write(str(input_data[counter]))
            if printExtraLines:
                sys.stdout.write("\n")
            counter += 1
    else:
        for line in input_data:
            sys.stdout.write(str(line))
            if printExtraLines:
                sys.stdout.write("\n")


if __name__ == "__main__":
    main()
