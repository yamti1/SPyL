from typing import Iterable


class UserSource:
    def __init__(self, iterable: Iterable):
        self._iterable = iterable

    def __iter__(self):
        return iter(self._iterable)
