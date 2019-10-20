#!/usr/bin/python3
import sys


def main():
        in_data = int(sys.stdin.readline())
       
        res = 1
        two = 0
        five = 0
        for i in range(2, in_data+1):
            tmp = i
            while(tmp % 2 == 0):
                tmp //= 2
                two += 1
            while(tmp % 5 == 0):
                tmp //= 5
                five += 1
            res *= tmp%1000
            res %= 1000
            
        while(two > five):
            res *= 2
            res %= 1000
            two -= 1
        print(res)


main() 
