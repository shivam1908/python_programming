def be_polite(fn):
    def wrapper():
        print('Hello there nice to meet you!')
        fn()
        print("have a good day")
    return wrapper

@be_polite
def greet():
    print("My ame is Shivam")
@be_polite
def rage():
    print("control your rage")

greet()
rage()