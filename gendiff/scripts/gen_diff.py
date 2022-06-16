#!/usr/bin/env python3
from gendiff.diff_generator import generate_diff
from gendiff.parser import parsing_args


def main():
    first, second, format = parsing_args()
    print(generate_diff(first, second, format))


if __name__ == '__main__':
    main()
