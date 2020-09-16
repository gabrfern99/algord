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
        sortMethods.insertion_sort(retlist)
        end = time.time()
    elif(method == "2"):
        start = time.time()
        sortMethods.selection_sort(retlist)
        end =  time.time()
    elif(method == "3"):
        start = time.time()
        sortMethods.merge_sort(retlist)
        end = time.time()
    elif(method == "4"):
        start = time.time()
        sortMethods.quick_sort(retlist, 0, len(retlist) - 1)
        end = time.time()
    for i in range(len(retlist)):
        print(retlist[i])
    print("\nTime elapsed:", end - start)

if __name__ == "__main__":
    main()
    exit(1)
