#!/usr/bin/env python3
from gendiff.diff_generator import generate_diff
from gendiff.cli import parsing_args


def main():
    args = parsing_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
