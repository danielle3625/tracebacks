import sys
import inspect
from pprint import pprint
from collections import Counter

# Create an empty counter

counter = Counter()

# Define the trace program. It will execute everytime sys.settrace is called.
# We want to populate counter with 'filepath/lineno': count for every frame executed beneath the hood.

def trace(frame, event, arg):
    lineno = frame.f_lineno
    filename = frame.f_code.co_filename
    
    info = f"TRACE: {event} - {filename}:{lineno}"
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
        y = []
        with open(filename) as file:
            for x in file:
                y.append(x)
            print(y[lineno])
            counter[filename, lineno] += 1
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
        

def main():
    sys.settrace(trace(frameinfo.frame, 'line', None) for frameinfo in inspect.getouterframes(inspect.currentframe())][:-1])
    
    
if __name__ == "__main__":
    main()

main()