#!/usr/bin/python3

import sys
from functools import reduce 
import math 

def area( q ):
    # area of a cyclic quadrilateral given four sides
    # using Brahmagupta's formula 
    # A = sqrt( (s-a)(s-b)(s-c)(s-d) ), where a,b,c,d are the four side lengths
    s = sum(q) / 2 # semiperimeter
    return math.sqrt(reduce(lambda x,y: x*y,  map(lambda l: (s - l), q)))
    
    

def main():
    q = list(map(int, sys.stdin.readline().split( " " )))
    print(area(q))
    




if __name__ == "__main__":
    main()
