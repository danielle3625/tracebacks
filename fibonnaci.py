import inspect
import sys
from pprint import pprint

# Because someone helped walk me through the same exercise via the recursive factorial function,
# I attempted to write a recursive fibonacci function on my own without any help/assistance, and 
# again use the helper function to print out each frame to understand the steps the computer is taking
# Writing the recursive fibonacci function proved to be harder for me than I thought it would be! 
# See fibonnaci.md for my thought process breakdown

def fib(n):
    pprint([helper(frameinfo.frame) for frameinfo in inspect.getouterframes(inspect.currentframe())][:-1])
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def helper(frame):
    return (frame.f_code.co_name, frame.f_locals, frame.f_lineno)
    
print(fib(4))
    


