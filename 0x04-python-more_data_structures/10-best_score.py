#!/usr/bin/python3
def best_score(a_dictionary):
    keys_list = list(a_dictionary.keys())
    higher_value = a_dictionary[keys_list[0]]
    key = ""

    for i in keys_list:
        if a_dictionary[i] > higher_value:
            key = i

    return (key)
