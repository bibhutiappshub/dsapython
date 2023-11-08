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


asc_num_list = [5, 6, 25, 38, 54, 88, 94]
desc_num_list = [94, 88, 54, 38, 25, 6, 5]
item = 5
asc_item_result = binary_search(asc_num_list, item, get_item_position_in_ascending_list)
desc_item_result = binary_search(desc_num_list, item, get_item_position_in_descending_list)

print("Ascending list item position:", asc_item_result)
print("Descending list item position:", desc_item_result)