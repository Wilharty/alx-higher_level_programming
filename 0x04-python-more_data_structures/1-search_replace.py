#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''function that replaces all occurrences of an element by another in a new list'''
    return [replace if element == search else element for elememt in my_list]
