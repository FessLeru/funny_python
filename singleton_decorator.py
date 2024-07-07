import functools


def singleton(cls):
    instance = None

    @functools.wraps(cls)
    def inner(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        return instance

    return inner


@singleton
class Noop:
    """I do nothing at all"""


# test
print(id(Noop()))
print(id(Noop()))
