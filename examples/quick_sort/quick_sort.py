def qsort(lst):
    if len(lst) < 2:
        return lst
    
    first_item = lst[0]
    rest_of_list = lst[1:]
    
    smaller_than_first = [k for k in rest_of_list if k <= first_item]
    larger_than_first = [k for k in rest_of_list if k > first_item]
    
    return qsort(smaller_than_first) + [first_item] + qsort(larger_than_first)
