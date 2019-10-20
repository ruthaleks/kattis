#!/usr/bin/python3
import sys 

def read_input():
    sys.stdin.readline() # N, not used
    k = list(map(lambda i : int(i), sys.stdin.readline().split()))
    return k

def main(): 
    k = read_input()    
    
    print(abs(sum(list(filter(lambda i : i < 0, k)))))


main()
