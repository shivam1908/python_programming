from time import time
from functools import wraps


def time_elapsed(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start_time = time()
        result = fn(*args, **kwargs)      # * -- used to uncouple tuple -- args and ** to uncouple kwargs   arguments respectively
        end_time =time()
        print(f"Time Elapsed : {end_time - start_time}")
        return result
    return wrapper

@time_elapsed
def sum_nums(end1):
    return sum(x for x in range(end1))

print(f"sum is : {sum_nums(5000000)}")