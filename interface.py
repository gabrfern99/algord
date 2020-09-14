# import sort_methods
import os.path

def print_methods():
    print("Avaiable sorting methods:\n1 - insertion_sort\n2 - selection_sort\n3 - merge_sort\n4 - quick_sort")

def interface_cli():
    file_exist = 0
    correct_option = 0
    while file_exist == 0:
        try:
            path = input("File path: ")
        except KeyboardInterrupt:
            pass
        if(os.path.isfile(path)) == True:
            file_exist = 1
            pass
        else:
            print("File don't exist, please, enter the correct path.")
    while correct_option == 0:
        try:
            print_methods()
            sort_method = input("Sort method to be used: ")
        except (ValueError, UnboundLocalError, KeyboardInterrupt):
            pass
        try:
            if(sort_method == "1" or sort_method == "2" \
               or sort_method == "3" or sort_method == "4"):
                correct_option = 1
                pass
            else:
                print("Please, enter the correct method option.")
        except UnboundLocalError:
            pass
    return path, sort_method


def csv_parser():
    path, method = interface_cli()
    csv_element_list = []
    line_count = 0
    with open(path, "r") as f:
        for line in f:
            line = line.strip("\n")
            csv_element_list.append(line)
    f.close()
    return csv_element_list, method
