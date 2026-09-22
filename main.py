from logger import log_decorator

if __name__ == "__main__":
    @log_decorator
    def sum_numbers(a, b):
        return a + b

    @log_decorator
    def hello(name):
        return f"Hello, {name}!"

    print(sum_numbers(5, 3))
    print(hello("World"))