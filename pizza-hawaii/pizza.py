#!/usr/bin/python3
import  sys
import copy
def read_in_data(number_of_pizzas):
    pizza_list = [] # includes (ing_german, ing_english) for each pizza
    for n in range(number_of_pizzas):
        sys.stdin.readline() # pizza name, not used
        ing_german = sys.stdin.readline().split()[1:] 
        ing_english = sys.stdin.readline().split()[1:]
        pizza_list.append((ing_german, ing_english))
    return pizza_list


def all_ingredients(pizza_list):
    eng_set = set()
    ger_set = set()

    for i in pizza_list:
        ger_list = i[0]
        eng_list = i[1]
        for j in ger_list:
            ger_set.add(j)
        for y in eng_list:
            eng_set.add(y)
    return list(eng_set), list(ger_set)


def match_ingredients(D, pizza_list):
    for i in pizza_list:
        ger_list = i[0]
        eng_list = i[1]
        for ger_ing in ger_list:
            if ger_ing not in D: 
                D[ger_ing] = copy.copy(eng_list) 
            else:
                for eng_ing in copy.copy(D[ger_ing]):
                    if eng_ing not in eng_list:
                        D[ger_ing].remove(eng_ing)
    return D

def ger_check(D, ger, pizza_list):
    for ger_ing in ger:
        for i in pizza_list:
            ger_list = i[0]
            eng_list = i[1]
            if ger_ing not in ger_list:
                for eng_ing in eng_list:
                    if eng_ing in D[ger_ing]:
                        D[ger_ing].remove(eng_ing)
                
    return D


def print_results(D, ger):
    l = []
    for i in ger:
        for j in D[i]:
            l.append((i, j))
    l.sort()
    for t in l:
        print("(" + str(t[0]) + ", " +str(t[1]) + ")")



def main():
    test_cases = int(sys.stdin.readline())
    for test in range(test_cases):
        number_of_pizza = int(sys.stdin.readline()) # number of pizzas
        D = {} # key: ingredient in german, value: list of ingredient in english
        all_geman_ingredients = set() # all german ingredients for each test case 
        
        pizza_list = read_in_data(number_of_pizza)  
        eng, ger = all_ingredients(pizza_list)
        ger.sort() 
        D = match_ingredients(D, pizza_list)
        D = ger_check(D, ger, pizza_list)
        print_results(D, ger)
        if test != test_cases-1:
            print("\n", end="")


                

main()


            


