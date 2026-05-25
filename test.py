


def main(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 10
    return wrapper

def main2(a):
    def inner(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) + a
        return wrapper
    return inner

@main
def test1(a,b):
    return a + b

@main2(50)
def test2(m,n):
    return m * n


print(test2(2, 3))