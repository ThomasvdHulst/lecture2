def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

@announce #add the announce function to the function
def hello():
    print("Hello!")

hello()
