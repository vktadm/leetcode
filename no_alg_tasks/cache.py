from functools import wraps


def make_key(args, kwargs):
    # kwargs сортируем, чтобы порядок не влиял на ключ
    return (args, tuple(sorted(kwargs.items())))


def cache_decorator(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = make_key(args, kwargs)

        if key in cache:
            return cache[key]

        result = func(*args, **kwargs)
        cache[key] = result
        return result

    # доступ к кэшу
    wrapper.cache = cache
    wrapper.get = lambda key: cache.get(key)

    # удобный метод для получения через args/kwargs
    wrapper.make_key = make_key

    return wrapper


@cache_decorator
def mul(a, b=1):
    return a * b
