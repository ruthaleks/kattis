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
    
    indata = sys.stdin.read()[:-1]
    number_list = list(map(valid_numbers.get, split_numbers(indata)))
    
    number = int("".join(map(str, filter(bool, number_list))))

    if None in number_list:
        print("BOOM!!")
    elif (number % 6) == 0:
        print("BEER!!")
    else: 
        print("BOOM!!")


    
main()