#!/usr/bin/env python3
from gendiff.generate_diff import generate_diff
from gendiff.parsing_args import parsing_args


def main():
    first, second, format = parsing_args()
    print(generate_diff(first, second, format))


if __name__ == '__main__':
    main()
