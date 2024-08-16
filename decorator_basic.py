def be_polite(fn):
    def wrapper():
        print("Hello there nice to meet you!")
        fn()
        print("have a great Day")
    return wrapper
def greet():
    print("My name is Shivam")

greet = be_polite(greet)

greet()
greet()