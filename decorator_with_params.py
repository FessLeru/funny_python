from typing import Any, TextIO
import functools
import sys

# it can be added 
trace_enable = True 


def trace(func: callable = None, *, file: str | TextIO | None = sys.stdout) -> callable:
    if func is None:
        return lambda func: trace(func, file=file)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(func.__name__, args, kwargs, file=file)
        return func(*args, **kwargs)

    return inner


@trace(file=sys.stderr)
def identity(x: Any = None) -> Any:
    """I do nothing useful"""
    return x


print(identity(x=42))
