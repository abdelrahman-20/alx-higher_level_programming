#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_dic = list(a_dictionary.keys())
    ord_dic = ord_dic.sort()
    for i in ord_dic:
        print("{}: {}".format(i, a_dictionary.get(i)))
