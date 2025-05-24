import functools
import time


def timer(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result =func(*args, **kwargs)
        stop = time.time()
        print(f"[TIMER] {func.__name__} ran in {stop - start: .4f}s")
        return result
    return wrapper

        
