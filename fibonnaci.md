i am trying to do the same practice problem we did yesterday on my own, since you had to baby bird me yesterday. This time, instead of a recursive factorial function, I decided to do a recursive fibonacci function. To begin, I wrote  a fibonacci function the way my brain naturally went about solving the question: 
```py
def fib(n):
     a, b = 0, 1
    fib_list = []
    while a < n:
      fib_list.append(a)
      a, b = b, a+b
    return fib_list
```
Then,  I tried to write another, but just print the values this time instead of returning a list
```py
def fib_func_two(n):
  a,b = 0,1
  for i in range(n+1):
    print(a)
    a, b = b, b+a
```
Now, I had no idea how to create a function that called itself to come up with the same thing. I found some plain text, but could not understand what was happening. I found a few different examples of 'recursive fibonacci python'
```py
def fib(n):
    if n < 0:
        print('please use a positive int')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```
now, i understood why I needed the program to return 0 if 0, or 1 if 1 (or so i thought), but what I did not understand was the `else` statement. 
* In my brain, I was imagining the frames in the computer to go as follows:
1. User calls fib(10)
2. 10 is > 0, and not ==0 nor ==1, thus the if and both elif statements are SKIPPED
3. ((10-1) + (10-2)) = 17 → WHAT! this is wrong

Then, I actually RAN the code, and noticed that the output number was 55! hmm...not 17 like I had computed in my head. This is the 10th index position of the fibonacci sequence that I generated above. How does this work!?!?!?

Since I could not figure out what was happening on my own, I looked for a video explanation.  I ended up here, attempting to find someone who can break down what is happening: https://www.youtube.com/watch?v=A3VQmxoWLHY

I learned that I was not taking into account that in frame #3 above (per my head): It wasn't just 9 + 8, it was fib(9) + fib(8), which then turns into fib(8) + fib(7), and ultimately ends up returning the base cases of `return 1` a bunch of times that ultimately add up to 55. Cool!

Additionally, I was able to simplify my recursive fibonacci function to:
```py
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
```
From here, implementing the helper function previously written was fairly straightforward:
```py
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
```

and the output!

```py
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\User\desktop\pythonstuff\traceback> & C:/Users/User/AppData/Local/Programs/Python/Python310/python.exe c:/Users/User/desktop/pythonstuff/traceback/fibonnaci.py
[('fib', {'n': 4}, 12)]
[('fib', {'n': 3}, 12), ('fib', {'n': 4}, 16)]
[('fib', {'n': 2}, 12), ('fib', {'n': 3}, 16), ('fib', {'n': 4}, 16)]
[('fib', {'n': 1}, 12),
 ('fib', {'n': 2}, 16),
 ('fib', {'n': 3}, 16),
 ('fib', {'n': 4}, 16)]
[('fib', {'n': 0}, 12),
 ('fib', {'n': 2}, 16),
 ('fib', {'n': 3}, 16),
 ('fib', {'n': 4}, 16)]
[('fib', {'n': 1}, 12), ('fib', {'n': 3}, 16), ('fib', {'n': 4}, 16)]
[('fib', {'n': 2}, 12), ('fib', {'n': 4}, 16)]
[('fib', {'n': 1}, 12), ('fib', {'n': 2}, 16), ('fib', {'n': 4}, 16)]
[('fib', {'n': 0}, 12), ('fib', {'n': 2}, 16), ('fib', {'n': 4}, 16)]
3
PS C:\Users\User\desktop\pythonstuff\traceback> 
```

