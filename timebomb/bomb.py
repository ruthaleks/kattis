#!/usr/bin/python3

import sys

import itertools as it

numbers = """
***   * *** *** * * *** *** *** *** ***
* *   *   *   * * * *   *     * * * * *
* *   * *** *** *** *** ***   * *** ***
* *   * *     *   *   * * *   * * *   *
***   * *** ***   * *** ***   * *** ***
"""

def split_numbers(numbers: str):
    v = list(zip(*numbers.split("\n")))

    def ignore_last(seq):
        return seq[:-1]

    return tuple(map(ignore_last, it.zip_longest(*[iter(v)] * 4 )))
        


def main():
    valid_numbers = dict(map(reversed, enumerate(split_numbers(numbers.strip()))))
    
    indata = sys.stdin.read().strip()
    print(split_numbers(indata))
    number = list(map(valid_numbers.get, split_numbers(indata)))
    print(number)


    
main()