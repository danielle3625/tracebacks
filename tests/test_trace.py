from codeinsights.trace import time_elapsed

def test_time_elapsed_is_positive():
    assert time_elapsed() > 0