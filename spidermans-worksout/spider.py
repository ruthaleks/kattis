#!/usr/bin/python3
import sys
import queue

class Node: 
    def __init__(self, value, option, max_value, index, c):
        self.value = value
        self.option = option
        self.max_value = max_value
        self.index = index
        self.c = c


def add_state(value, option, max_value, index, stopIndex, D, q, c):
    n = Node(value, option, max_value, index, c)
    c += 1
    D[(index, value)] = n
    if(index < stopIndex):
        q.put((n.max_value, n.c, n))
    return c


def check_state(key, D):
    if key not in D:
        return True
    else:
        return False
    
def update_state(n, p, opt):
    if (p.max_value < n.max_value):
        n.max_value = max(n.value, p.max_value)
        n.option = p.option + opt

def main():
    for i in sys.stdin:
        N = int(i) # number of test scenarios
        
        for i in range(N):
            c = 0
            M = int(sys.stdin.readline()) # number of distances
            data = sys.stdin.readline().split()
            D = {} #Dict for saving optimal values, key = (index, value) 
            q = queue.PriorityQueue()
            
            c = add_state(int(data[0]), "U", int(data[0]), 0, M-1, D, q, c)
        

            while not q.empty():
                (v, a, p) = q.get()
                d = int(data[p.index + 1]) 

                # Up
                h = p.value + d
                if ( check_state((p.index+1, h), D)):
                    c = add_state(h, p.option+"U", max(h, p.max_value), p.index + 1, M-1, D, q, c)
                else:
                    update_state(D[(p.index+1, h)], p, "U")

                #Down
                if(p.value >= d):
                    h = p.value - d
                    if ( check_state((p.index+1, h), D)):
                        c = add_state(h, p.option+"D", max(h, p.max_value), p.index + 1, M-1, D, q, c)
                    else:
                        update_state(D[(p.index+1, h)], p, "D")
                if not (check_state((M-1, 0), D)):
                    break
            if(check_state((M-1, 0), D)):
                print("IMPOSSIBLE")
            else:
                print(D[(M-1, 0)].option)



main()
