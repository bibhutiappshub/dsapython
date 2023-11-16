# Naive approach
def brute_force_approach(num_rotated_list):
    for idx, elem in enumerate(num_rotated_list):
        if idx != len(num_rotated_list)-1 and num_rotated_list[idx] > num_rotated_list[idx+1]:
            return idx+1

    return 0

# Optimized Approach
def get_min_num_rotations(num_rotated_list):
    start = 0
    end = len(num_rotated_list) - 1
    item = num_rotated_list[0]
    num_rotations = 0

    if num_rotated_list[0] < num_rotated_list[end]:
        return num_rotations
    else:
        while start <= end:
            mid = (start+end) // 2
            if num_rotated_list[mid] >= item and start == end:
                return mid + 1
            elif num_rotated_list[mid] > item:
                start = mid + 1
                item = num_rotated_list[mid]
                num_rotations = mid
            elif num_rotated_list[mid] <= item and start == end:
                return num_rotations + 1
            elif num_rotated_list[mid] < item:
                end = mid - 1

    return num_rotations

rotated_list = [6, 9, 0, 2, 3, 4, 5]
naive_num_rotations = brute_force_approach(rotated_list)
optimised_num_rotations = get_min_num_rotations(rotated_list)
print(naive_num_rotations)
print(optimised_num_rotations)