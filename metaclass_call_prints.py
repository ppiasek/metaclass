from functools import wraps


def print_deco(func):
    if type(func) == type or func.__qualname__ == "Logger":
        print(f"\nClass {func.__qualname__} registered.\n")

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__qualname__}() called with args:\n\t{func.__qualname__.replace(f'.{func.__name__}', '')}, {str(args[1:])}")
        result = func(*args, **kwargs)
        print(f"\tResult of {func.__qualname__}: {result}")
        return result
    return wrapper


@print_deco
class Singleton(type):
    _instances = {}

    @print_deco
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @print_deco
    def __new__(cls, *args, **kwargs):
        cls.__new__.called = True
        return super().__new__(cls, *args, **kwargs)

    @print_deco
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

    @print_deco
    def mro(self, *args, **kwargs):
        return super().mro(*args, **kwargs)

    @print_deco
    def __prepare__(self, *args, **kwargs):
        return {}


@print_deco
class Logger(metaclass=Singleton):
    @print_deco
    def __init__(self):
        super().__init__()

    @print_deco
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


print("\nFirst instance:\n")
Logger()
print("\nSecond instance:\n")
Logger()
