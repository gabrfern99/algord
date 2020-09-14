#!/usr/bin/python3

import sortMethods
import interface

def main():
    list, method = interface.csv_parser()
    if(method == "1"):
        sortMethods.insertion_sort(list)
    elif(method == "2"):
        sortMethods.selection_sort(list)
    elif(method == "3"):
        sortMethods.merge_sort(list)
    for i in range(len(list)):
        print(list[i])

if __name__ == "__main__":
    main()
