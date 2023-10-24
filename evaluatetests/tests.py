import time

RED = '\033[91m'
GREEN = '\033[32m'
END = '\033[0m'
BOLD = '\033[1m'


def print_result(test_input, actual_output, execution_time, is_passed):
    print(f"""
            Input:
                {test_input["input"]}
                
            Expected Output:
                {test_input["output"]}
                
            Actual Output:
                {actual_output}
                
            Execution Time:
                {execution_time}ms
                
            Test Result: {f"{BOLD}{GREEN}PASSED{END}" if is_passed else f"{BOLD}{RED}FAILED{END}"}
        """)


def print_test_summary(total_tests, success_tests, failed_tests):
    print(f"{BOLD}SUMMARY:{END}")
    print(f"{BOLD}TOTAL:{END} {total_tests} {BOLD}{GREEN}PASSED:{END} {success_tests} {BOLD}{RED}FAILED:{END} {failed_tests}")


def evaluate_tests(func, tests):
    total_tests = len(tests)
    success_tests = 0
    failed_tests = 0
    is_passed = False

    if type(tests) == dict:
        result, exec_time = get_func_execution_time(func, tests)
        print_result(tests, result, exec_time)
    else:
        for idx, test in enumerate(tests):
            print(f"{BOLD}TEST CASE #{idx}{END}")
            result, exec_time = get_func_execution_time(func, test)

            if test["output"] == result:
                success_tests += 1
                is_passed = True
            else:
                failed_tests += 1
                is_passed = False

            print_result(test, result, exec_time, is_passed)

    print_test_summary(total_tests, success_tests, failed_tests)


def get_func_execution_time(func, test):
    start = time.time()
    result = func(test)
    end = time.time()
    exec_time = end-start
    return result, exec_time