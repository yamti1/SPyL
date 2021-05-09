from dataclasses import dataclass
from typing import Iterator, Callable, Union

from .commands import dedup, print_gen
from .filter import Filter


@dataclass
class Search:
    _pipeline: Iterator[dict]

    def dedup(self, *args, **kwargs) -> 'Search':
        self._pipeline = dedup(self._pipeline, *args, **kwargs)
        return self

    def transaction(self, *args, **kwargs) -> 'Search':
        pass

    # TODO: test
    def filter(self, arg: Union[dict, Callable]) -> 'Search':
        self._pipeline = filter(Filter(arg), self._pipeline)
        return self

    def out(self) -> 'Search':
        self._pipeline = print_gen(self._pipeline)
        return self

    def execute(self) -> None:
        for _result in self._pipeline:
            pass

    def results(self):
        yield from self._pipeline
