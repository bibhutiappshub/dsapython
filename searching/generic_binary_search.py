def get_item_position_in_ascending_list(input_list, mid_pos, target):
    if input_list[mid_pos] == target:
        return "found"
    elif input_list[mid_pos] > target:
        return "left"
    else:
        return "right"


def get_item_position_in_descending_list(input_list, mid_pos, target):
    if input_list[mid_pos] == target:
        return "found"
    elif input_list[mid_pos] < target:
        return "left"
    else:
        return "right"


def binary_search(input_list, target, get_item_position):
    start = 0
    end = len(input_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if get_item_position(input_list, mid, target) == "found":
            return mid
        elif get_item_position(input_list, mid, target) == "left":
            end = mid-1
        elif get_item_position(input_list, mid, target) == "right":
            start = mid+1

    return -1
