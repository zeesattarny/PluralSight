def noop(f):
    def noop_wrapper():
        return f()
    noop_wrapper.__name__ = f.__name__
    noop_wrapper.__doc__ = f.__doc__

def hello():
    "Print a well- known message."
    print('Hello, World!')

##################################################################################
import functools


def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    noop_wrapper.__name__ = f.__name__
    noop_wrapper.__doc__ = f.__doc__

def hello():
    "Print a well- known message."
    print('Hello, World!')
