# Challenge: Write a python function to index all items in a list that are equal to a given value.
# Input: list to search, value to search for
# Output: list of indices

def index_all(search_list, item):
    index_list = []
    for index, value in enumerate(search_list):
        if value == item:
            index_list.append([index])
        elif isinstance(search_list[index], list):
            for i in index_all(search_list[index], item):
                index_list.append([index] + i)
    return index_list