from evaluatetests.tests import evaluate_tests
from test_cases import search_test_cases

def linear_search(test_input):
    pos = 0
    while pos < len(test_input["input"]["cards"]):
        if test_input["input"]["cards"][pos] == test_input["input"]["query"]:
            return pos
        pos += 1

    return -1

evaluate_tests(linear_search, search_test_cases)