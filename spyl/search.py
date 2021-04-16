from dataclasses import dataclass
from typing import Iterable

from .commands import dedup, print_gen


@dataclass
class Search:
    _pipeline: Iterable

    def dedup(self, *args, **kwargs) -> 'Search':
        self._pipeline = dedup(self._pipeline)
        return self

    def transaction(self, *args, **kwargs) -> 'Search':
        pass

    def out(self) -> 'Search':
        self._pipeline = print_gen(self._pipeline)
        return self

    def execute(self) -> None:
        for _result in self._pipeline:
            pass

    def results(self):
        yield from self._pipeline
