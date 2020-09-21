#!/usr/bin/python3
import sys
import sortMethods
import interface
import time

def main():
    retlist, method = interface.csv_parser()
    sys.setrecursionlimit(len(retlist))
    if(method == "1"):
        start = time.process_time()
        sortMethods.insertion_sort(retlist)
    elif(method == "2"):
        start = time.process_time()
        sortMethods.selection_sort(retlist)
    elif(method == "3"):
        start = time.process_time()
        sortMethods.merge_sort(retlist)
    elif(method == "4"):
        start = time.process_time()
        sortMethods.quick_sort(retlist, 0, len(retlist) - 1)
    for i in range(len(retlist)):
        print(retlist[i], time.process_time() - start, sep=" - Current time: ")
    print("\nTime elapsed:", time.process_time() - start)

if __name__ == "__main__":
    main()
