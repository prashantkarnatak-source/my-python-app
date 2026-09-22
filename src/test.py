def uppercase_decorator(func):
    def wrapper(name):
        result = func(name)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet(name):
    return f"Hello, {name}"

print(greet("alice"))