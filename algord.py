#!/usr/bin/python3

import sortMethods
import interface
import sys

def main():
    retlist, method = interface.csv_parser()
    sys.setrecursionlimit(len(retlist))
    if(method == "1"):
        sortMethods.insertion_sort(retlist)
    elif(method == "2"):
        sortMethods.selection_sort(retlist)
    elif(method == "3"):
        sortMethods.merge_sort(retlist)
    elif(method == "4"):
        sortMethods.quick_sort(retlist, 0, len(retlist) - 1)
    for i in range(len(retlist)):
        print(retlist[i])

if __name__ == "__main__":
    main()
