#!/usr/bin/python3
import sys

def main():
    indata = sys.stdin.readline().strip().split(' ')

    month = indata[0]
    day = int(indata[1])

    if (month == "DEC" and day == 25) or (month == "OCT" and day == 31):
        print("yup")
    else:
        print("nope")



main()