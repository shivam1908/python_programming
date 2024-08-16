def log_function_data(fn):
    def wrapper(*args,**kwargs):
        """This is wrapper function"""
        print(f"you are about to call {fn.__name__}")
        print( f'Here is the doc. for function : {fn.__doc__}')
        return fn(*args,**kwargs)
    return wrapper

@log_function_data
def add(num1, num2):
    """ Function return the sum of two numbers"""
    return num1+num2

# print(add(10,20))
# print(add.__doc__)    # it will print doc for wrapper instead of add -- to avoid this we need to use wrap to preserve the metadata
help(add)