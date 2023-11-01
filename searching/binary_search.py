from evaluatetests.tests import evaluate_tests
from test_cases import search_test_cases


def binary_search_recursion(test_input):
    cards_list = test_input["input"]["cards"]
    query = test_input["input"]["query"]
    startindex = 0
    endindex = len(cards_list) - 1

    def binary_search_helper(sorted_list, start, end, item):
        middle = (end + start) // 2

        if end >= start:
            if sorted_list[middle] == item:
                return middle
            elif sorted_list[middle] < item:
                end = middle - 1
                return binary_search_helper(sorted_list, start, end, item)
            elif sorted_list[middle] > item:
                start = middle + 1
                return binary_search_helper(sorted_list, start, end, item)
        else:
            return -1

    return binary_search_helper(cards_list, startindex, endindex, query)


def binary_search_iteration(test_input):
    sorted_list = test_input["input"]["cards"]
    query = test_input["input"]["query"]
    start = 0
    end = len(sorted_list) - 1

    while start <= end:
        middle = (end + start) // 2

        if sorted_list[middle] == query:
            return middle
        elif sorted_list[middle] < query:
            end = middle - 1
        elif sorted_list[middle] > query:
            start = middle + 1

    return -1


# evaluate_tests(binary_search_iteration, search_test_cases)
evaluate_tests(binary_search_recursion, search_test_cases)
