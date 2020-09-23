#!/usr/bin/python3
import sys
import sortMethods
import interface
import time

def main():
    retlist, method = interface.csv_parser()
    header = retlist[0]
    retlist = retlist[1:]
    sys.setrecursionlimit(len(retlist))

    if(method == "1"):
        start = time.process_time()
        comps, moves = sortMethods.insertion_sort(retlist)
    elif(method == "2"):
        start = time.process_time()
        comps, moves = sortMethods.selection_sort(retlist)
    elif(method == "3"):
        start = time.process_time()
        comps, moves = sortMethods.merge_sort(retlist)
    elif(method == "4"):
        start = time.process_time()
        comps, moves = sortMethods.quick_sort(retlist, 0, len(retlist) - 1)
    print(header)
    for i in range(len(retlist)):
        print(retlist[i], time.process_time() - start, sep=" - Current time: ")
    print("\nTime elapsed:", time.process_time() - start)
    print("Comparisons: %d\nMovements: %d\n" % (comps, moves))



if __name__ == "__main__":
    main()
    exit(1)
