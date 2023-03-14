
def is_in_previous(two_dimensional_list, value):
    return any(
        value in nested_list
        for nested_list in two_dimensional_list
    )

def get_index(list, value):
    x = [x for x in list if value in x][0]
    return list.index(x)