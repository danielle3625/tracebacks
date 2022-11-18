import sys

# This is an example to help understand sys.settrace

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
        

def demo():
    for x in range(5):
        y = x
    
    try:
        raise ValueError
    except ValueError:
        return 12


def main():
    sys.settrace(trace)
    
    x = 2  # this won't be traced, since the trace function was not set before main() called
    
    demo()
    
    sys.settrace(None)

    
if __name__ == "__main__":
    main()

main()