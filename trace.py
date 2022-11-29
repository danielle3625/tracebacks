import sys
from pprint import pformat
from collections import Counter, defaultdict
from logging import getLogger, StreamHandler, DEBUG
import json
import blackjack
import time

LOG = getLogger(__name__)

# Create an empty counter 
# Global dictionary with tuple keys
# This will tracke linenum per filename

counter = Counter()

# Store Global Time variable
time_start = time.time_ns()

# Store Elapsed time values per frame
time_counter = defaultdict(float)

# Track previous file line, since time elapsed will track previous frame time
fileline = 'firstframe'


def time_elapsed():
    global time_start
    current_time = time.time_ns()

    elapsed = current_time - time_start

    time_start = time.time_ns()

    return elapsed


# Define the trace program. It will execute everytime sys.settrace is called.
# We want to populate counter with 'filepath/lineno': count for every frame executed beneath the hood.

def trace(frame, event, arg):
    global fileline
    lineno = frame.f_lineno
    filename = frame.f_code.co_filename
  
    
    info = f"TRACE: {event} - {filename}:{lineno}"
    LOG.debug(info)



    time_counter[fileline] += time_elapsed()

    
    fileline = f'FILE NAME:{filename} LINENUM:{lineno}'

    if event == "call":
        # A function is called
        # arg is None
        # return value specifies the new local trace
        # function
        time_elapsed()
        return trace
    elif event == "line":
        # The interpreter is about to execute a new line of code
        # arg is None
        # return value specifies the new local trace function
        y = []
        with open(filename) as file:
            for x in file:
                y.append(x)
            counter[filename, lineno] += 1
        return trace
    elif event == "return":
        # arg is the value that will be returned, or None if the event is caused by an exception being raised
        # return value is unused
        LOG.debug(f"  was exception: {arg is None}")
    elif event == "exception":
        # An exception has occurred
        # arg is a tuple: (exception, value, traceback)
        # return value specifies the new local trace function
        LOG.debug(f"  exc info: {arg}")
        return trace
    elif event == "opcode":
        # The interpreter is about to execute a new opcode
        # arg is None
        # return value specifies the new local trace function
        return trace
    else:
        raise ValueError("Uknown trace event type")
        

def main():
    root_logger = getLogger()
    root_logger.setLevel(DEBUG)

    handler = StreamHandler()
    handler.setLevel(DEBUG)

    root_logger.addHandler(handler)

    sys.settrace(trace)
    blackjack.blackjack_play_game()
    sys.settrace(None)
    LOG.info(pformat(counter))
    LOG.info(pformat(time_counter))

    def json_dumps_tuple_keys(mapping):
        string_keys = {json.dumps(k): v for k, v in mapping.items()}
        return json.dumps(string_keys, indent=4)
    
    json_object_filelines = json_dumps_tuple_keys(counter)
    json_object_time = json_dumps_tuple_keys(time_counter)
    with open("tracedata.json", 'w') as outfile:
        outfile.write(json_object_filelines)
        outfile.write(json_object_time)
    
    
if __name__ == "__main__":
    main()
