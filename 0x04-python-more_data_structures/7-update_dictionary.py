#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_diction:
        a_dictionary[key] = value
    else:
        for i in a_dictionary:
            if i == key:
                a_dictionary[i] = value
    return 
