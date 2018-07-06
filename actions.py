# Action function dictionary used in solver.py
ACTIONS = {
    'add': lambda a, n: add(a, n),
    'subtract': lambda a, n: subtract(a, n),
    'divide': lambda a, n: divide(a, n),
    'multiply': lambda a, n: multiply(a, n),
    'append': lambda a, n: append(a, n),
    'square': lambda a, n: square(n),
    'flipsign': lambda a, n: flipsign(n),
    'backspace': lambda a, n: backspace(n),
    'reverse': lambda a, n: reverse(n)
}

## DEFINE ACTION FUNCTIONS

def multiply(a, n):
    return n * a

def divide(a, n):
    return float(n) / a

def add(a, n):
    return n + a

def subtract(a, n):
    return n - a

def append(a, n):
    if n < 0:
        a = -a
    
    return n*10 + a

def square(n):
    return n*n

def flipsign(n):
    return -n

def backspace(n):
    return n / 10

def reverse(n):
    return int(str(n)[::-1])