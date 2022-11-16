# tracebacks
# will update more later

factorial.py is an example of how to use sys.settrace(tracefunc) for identifying frames
a function that uses recursion to compute factorials is defined
then, a helper function is defined that returns a tuple displaying info on current frame and outer frames
this allows us to determine the frame sequences involved in the recursive factorial function
