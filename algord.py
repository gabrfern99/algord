#!/usr/bin/python3

import sortMethods
import interface
import sys

def main():
    retlist, method = interface.csv_parser()
    sys.setrecursionlimit(len(retlist))
    if(method == "1"):
        comps, moves = sortMethods.insertion_sort(retlist)
    elif(method == "2"):
        comps, moves = sortMethods.selection_sort(retlist)
    elif(method == "3"):
        comps, moves = sortMethods.merge_sort(retlist)
    elif(method == "4"):
        comps, moves = sortMethods.quick_sort(retlist, 0, len(retlist) - 1)
    for i in range(len(retlist)):
        print(retlist[i])
    print("Comparisons: %d\nMovements: %d\n" % (comps, moves))

if __name__ == "__main__":
    main()
