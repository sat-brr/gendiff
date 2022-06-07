#!/usr/bin/env python3
from gen_diff.engine import generate_diff
from gen_diff.parser import parsing


def main():
    first, second, format = parsing()
    print(generate_diff(first, second, format))


if __name__ == '__main__':
    main()
