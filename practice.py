def outer():
    def inner():
        print("Hello from inner")
    return inner

f = outer()
