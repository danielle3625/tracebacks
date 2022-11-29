import sys
from pprint import pformat
from collections import Counter
from logging import getLogger, StreamHandler, DEBUG
import json
import blackjack
import time

LOG = getLogger(__name__)

# Create an empty counter

counter = Counter()
time_start = time.time_ns()


def time_elapsed():
    global time_start
    current_time = time.time_ns()

    elapsed = current_time - time_start

    print('Elapsed Time = ', elapsed)


# Define the trace program. It will execute everytime sys.settrace is called.
# We want to populate counter with 'filepath/lineno': count for every frame executed beneath the hood.

def trace(frame, event, arg):
    lineno = frame.f_lineno
    filename = frame.f_code.co_filename
    
    info = f"TRACE: {event} - {filename}:{lineno}"
    LOG.debug(info)
    
    if event == "call":
        # A function is called
        # arg is None
        # return value specifies the new local trace function
        time_elapsed()
        return trace
    elif event == "line":
        # The interpreter is about to execute a new line of code
        # arg is None
        # return value specifies the new local trace function
        time_elapsed()
        y = []
        with open(filename) as file:
            for x in file:
                y.append(x)
            counter[filename, lineno] += 1
        time_elapsed()
        return trace
    elif event == "return":
        # arg is the value that will be returned, or None if the event is caused by an exception being raised
        # return value is unused
        LOG.debug(f"  was exception: {arg is None}")
        time_elapsed()
    elif event == "exception":
        # An exception has occurred
        # arg is a tuple: (exception, value, traceback)
        # return value specifies the new local trace function
        LOG.debug(f"  exc info: {arg}")
        time_elapsed()
        return trace
    elif event == "opcode":
        # The interpreter is about to execute a new opcode
        # arg is None
        # return value specifies the new local trace function
        time_elapsed()
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

    def json_dumps_tuple_keys(mapping):
        string_keys = {json.dumps(k): v for k, v in mapping.items()}
        return json.dumps(string_keys, indent=4)
    
    json_object = json_dumps_tuple_keys(counter)
    with open("tracedata.json", 'w') as outfile:
        outfile.write(json_object)
    
    
if __name__ == "__main__":
    main()
