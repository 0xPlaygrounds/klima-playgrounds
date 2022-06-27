import time
from functools import cache


def time_cache(seconds=3600):
    def decorator(func):
        @cache
        def extra_time_arg_func(time_key):
            return func()

        def wrapper():
            time_key = int(time.time() / seconds)
            return extra_time_arg_func(time_key)

        return wrapper

    return decorator
