import inspect
import sys
from pprint import pprint

# Here, We wrote used a helper function within a  recursive factorial function to get a printout of frames in order that computer went through to compute the problem

# This is an attempt to implement the trace function instead of the helper function

def factorial(n):
    print('restart')
    pprint([trace(frameinfo.frame, 'line', None) for frameinfo in inspect.getouterframes(inspect.currentframe())][:-1])
    if n == 0:
        return 1
    return n * factorial(n - 1)

def helper(frame):
    return (frame.f_code.co_name, frame.f_locals, frame.f_lineno)

def trace(frame, event, arg):
    lineno = frame.f_lineno
    filename = frame.f_code.co_filename
    
    info = f"TRACE: {event}, FUNCTION NAME:{frame.f_trace} CODE NAMES {frame.f_code}- {filename}:{lineno}"
    print(info)
    
    if event == "call":
        # A function is called
        # arg is None
        # return value specifies the new local trace function
        return trace
    elif event == "line":
        # The interpreter is about to execute a new line of code
        # arg is None
        # return value specifies the new local trace function
        return trace
    elif event == "return":
        # arg is the value that will be returned, or None if the event is caused by an exception being raised
        # return value is unused
        print(f"  was exception: {arg is None}")
    elif event == "exception":
        # An exception has occurred
        # arg is a tuple: (exception, value, traceback)
        # return value specifies the new local trace function
        print(f"  exc info: {arg}")
        return trace
    elif event == "opcode":
        # The interpreter is about to execute a new opcode
        # arg is None
        # return value specifies the new local trace function
        return trace
    else:
        raise ValueError("Uknown trace event type")


print(factorial(7))