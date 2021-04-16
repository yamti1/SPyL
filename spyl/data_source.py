import csv
from typing import Iterable


class CSV(Iterable):
    def __init__(self, filename: str, *args, **kwargs):
        self._filename = filename
        self._args = args
        self._kwargs = kwargs

    def __iter__(self):
        with open(self._filename, newline='') as csv_file:
            reader = csv.DictReader(csv_file, *self._args, **self._kwargs)
            yield from reader
