#!/usr/bin/python3

import sys

def divide(l):
    idx = int((len(l))/2) 
    return (l[0:idx], l[idx:])

def convert_to_chr(i):
    v = i - ord('A')  
    if v > 25:
        return chr( v%26 + ord('A') )
    else:
        return chr(i)

def rotate(tup):
    res = []
    for t in tup:
        rv = sum(list(map(lambda i: ord(i)-ord('A'), t)))
        v1 = map( lambda x : x + rv, map(ord, t))
        res.append(list(map( convert_to_chr , v1 ))) 
    return res

def merge( tup ):
    ov = list(map( lambda x: ord(x)-ord('A'), tup[1]))
    msg = []
    for i in range(len(ov)):
        msg.append(ord(tup[0][i]) + ov[i])
    return ''.join(map(str,(map(convert_to_chr, msg))))


def main(): 
    encryp_msg = list(sys.stdin.readline())[:-1]

    print(merge(rotate(divide(encryp_msg))))

main()

