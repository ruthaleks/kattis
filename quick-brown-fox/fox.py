#!/usr/bin/python3

import string
import sys

def solve(line: str) -> str:
    def is_letter(c):
        return c in string.ascii_lowercase
        
    letters = set(filter(is_letter, line.lower()))
    diff = set(string.ascii_lowercase) - letters
    
    if not diff:
        return "pangram"

    sorted_diff = "".join(sorted(diff))
    return f"missing {sorted_diff}"

def main():
    indata = sys.stdin.readlines()[1:]
    print("\n".join(map(solve, indata)))

if __name__ == "__main__":
    main()