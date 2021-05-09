from typing import List, Iterator


class _Transaction(dict):
    pass


def transaction(generator: Iterator[dict], *fieldnames):
    transactions: List[_Transaction] = []

    for event in generator:

