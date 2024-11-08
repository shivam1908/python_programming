from functools import wraps
# wrap preserves a function's metadata when it is decorated

# def my_decorator(fn):
#     @wraps(fn)
#     def wrapper(*args,**kwargs):
#         pass
#     return wrapper

def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        """This is wrapper function"""
        print(f"you are about to call: {fn.__name__} ")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args,**kwargs)
    return wrapper

@log_function_data
def add(num1, num2):
    """"This function adds two functions"""
    return num1+num2

print(add(10,20))
print(add.__name__)
print(add.__doc__)

