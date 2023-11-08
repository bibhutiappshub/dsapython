from searching.generic_binary_search import binary_search


def get_first_position(input_list, mid_pos, target):
    if input_list[mid_pos] == target and mid_pos != 0 and input_list[mid_pos-1] == target:
        return "left"
    if input_list[mid_pos] == target:
        return "found"
    elif input_list[mid_pos] > target:
        return "left"
    else:
        return "right"


def get_last_position(input_list, mid_pos, target):
    if input_list[mid_pos] == target and mid_pos != len(input_list) - 1 and input_list[mid_pos+1] == target:
        return "right"
    if input_list[mid_pos] == target:
        return "found"
    elif input_list[mid_pos] > target:
        return "left"
    else:
        return "right"


def find_start_end_position_of(a_number, in_sorted_array):
    first_pos = binary_search(in_sorted_array, a_number, get_first_position)
    last_pos = binary_search(in_sorted_array, a_number, get_last_position)
    return first_pos, last_pos


sorted_list = [7, 8, 9, 10, 10]
item_to_search = 8
result = find_start_end_position_of(item_to_search, sorted_list)
print(result)
