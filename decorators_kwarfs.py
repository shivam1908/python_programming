def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args,**kwargs).upper()     # *args-- tuple unpacking  **kwargs -- dictionary unpacking 
    return wrapper


@shout
def mad(name):
    return f"{name} is MAD"

@shout
def madat(p1,p2):
    return f"{p1} is MAD at {p2}"

print(mad("Monarch"))   # Monarch isadded to *args hence a tuple  

print(mad(name = "Monarch"))     # added to **kwargs hence dictionary unpacking

print(madat("Monarch",'Beru'))
print(madat(p2= 'Beru', p1 ='Monarch'))