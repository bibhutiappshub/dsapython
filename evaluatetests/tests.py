import time


def print_result(test_input, actual_output, execution_time):
    RED = '\033[91m'
    GREEN = '\033[32m'
    END = '\033[0m'
    BOLD = '\033[1m'

    print(f"""
            Input:
                {test_input["input"]}
                
            Expected Output:
                {test_input["output"]}
                
            Actual Output:
                {actual_output}
                
            Execution Time:
                {execution_time}ms
                
            Test Result: {f"{BOLD}{GREEN}PASSED{END}" if test_input['output'] == actual_output else f"{BOLD}{RED}FAILED{END}"}
        """)


def evaluate_tests(func, tests):
    if type(tests) == dict:
        result, exec_time = get_func_execution_time(func, tests)
        print_result(tests, result, exec_time)
    else:
        for idx, test in enumerate(tests):
            print(f"\033[1mTEST CASE #{idx}\033[0;0m")
            result, exec_time = get_func_execution_time(func, test)
            print_result(test, result, exec_time)


def get_func_execution_time(func, test):
    start = time.time()
    result = func(test)
    end = time.time()
    exec_time = float(end-start)
    return result, exec_time


def linear_search(test_input):
    pos = 0
    while pos < len(test_input["input"]["cards"]):
        if test_input["input"]["cards"][pos] == test_input["input"]["query"]:
            return pos
        pos += 1

    return -1


search_test_cases = [
    {"input": {"cards": [12, 8, 7, 5, 3], "query": 12}, "output": 0},
    {"input": {"cards": [35, 23, 16, 7, 1], "query": 1}, "output": 4},
    {"input": {"cards": [78, 67, 43, 25, 18], "query": 43}, "output": 2},
    {"input": {"cards": [23, 19, 17, 12, 0], "query": 19}, "output": 1},
    {"input": {"cards": [33, 16, 13, 9, 2], "query": 5}, "output": -1},
    {"input": {"cards": [58, 25, 47, 54, 89], "query": 54}, "output": -1},
    {"input": {"cards": [], "query": 10}, "output": -1},
    {"input": {"cards": [416, 203, 203, 105, 105, 92, 92], "query": 105}, "output": 3}
]

test = {"input": {"cards": [12, 8, 7, 5, 3], "query": 12}, "output": 0}

evaluate_tests(linear_search, search_test_cases)
# evaluate_tests(search_func, test)