#!/usr/bin/python3
import sys
import sortMethods
import interface
import time

def main():
    retlist, method = interface.csv_parser()
    sys.setrecursionlimit(len(retlist))
    if(method == "1"):
        start = time.time()
        comps, moves = sortMethods.insertion_sort(retlist, 0, 0)
        end = time.time()
    elif(method == "2"):
        start = time.time()
        comps, moves = sortMethods.selection_sort(retlist, 0, 0)
        end =  time.time()
    elif(method == "3"):
        start = time.time()
        comps, moves = sortMethods.merge_sort(retlist, 0, 0)
        end = time.time()
    elif(method == "4"):
        start = time.time()
        comps, moves = sortMethods.quick_sort(retlist, 0, len(retlist) - 1, 0, 0)
        end = time.time()
    for i in range(len(retlist)):
        print(retlist[i])
    print("Comparisons: %d\nMovements: %d\n" % (comps, moves))
    print("\nTime elapsed:", end - start)

if __name__ == "__main__":
    main()
    exit(1)