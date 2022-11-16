import inspect
import sys
from pprint import pprint

# Here, We wrote used a helper function within a  recursive factorial function to get a printout of frames in order that computer went through to compute the problem

def factorial(n):
    pprint([helper(frameinfo.frame) for frameinfo in inspect.getouterframes(inspect.currentframe())][:-1])
    if n == 0:
        return 1
    return n * factorial(n - 1)

def helper(frame):
    return (frame.f_code.co_name, frame.f_locals, frame.f_lineno)

print(factorial(7))


    


