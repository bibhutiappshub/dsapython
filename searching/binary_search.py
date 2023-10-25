def binary_search_using_recursion(sorted_list, start, end, item):
    middle = (end+start) // 2

    if(end >= start):
        if sorted_list[middle] == item:
            return middle
        elif sorted_list[middle] < item:
            end = middle - 1
            return binary_search_using_recursion(sorted_list, start, end, item)
        elif sorted_list[middle] > item:
            start = middle+1
            return binary_search_using_recursion(sorted_list, start, end, item)
    else:
        return -1


def binary_search_using_iteration(sorted_list, item):
    start = 0
    end = len(sorted_list) - 1

    while start <= end:
        middle = (end+start) // 2

        if sorted_list[middle] == item:
            return middle
        elif sorted_list[middle] < item:
            end = middle - 1
        elif sorted_list[middle] > item:
            start = middle + 1

    return -1

search_arr = [9, 7, 6, 4, 3, 2, 1]
query = 4
lowindex = 0
highindex = len(search_arr) - 1
recur_res = binary_search_using_recursion(search_arr, lowindex, highindex, query)
bin_res = binary_search_using_iteration(search_arr, query)
print("Recursion Result: ", recur_res)
print("Iterative Result: ", bin_res)
