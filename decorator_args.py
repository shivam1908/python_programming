def shout(fn):
    def wrapper(*args):
        print("hello there")
        return fn(*args).upper()
        
    return wrapper

@shout                              #decorator same as declaring warn = shout(warn)
def warn(name):
    return f" {name} is MAD!"

@shout                              #decorator same as declaring madat = shout(madat)  
def madat(person1, person2):
        return f"{person1} is MAD at {person2}"


#warn = shout(warn)     --- replace by decorator @shout
#madat = shout(madat)   --- replace by decorator @shout
print(warn("Monarch"))
print(madat("Monarch","Beru"))
