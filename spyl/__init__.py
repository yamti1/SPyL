def _dedup(generator):
    s = set()
    for event in generator:
        if event in s:
            continue
        s.add(event)
        yield event


def _print(generator):
    for event in generator:
        print(event)
        yield event


class SPyLSearch:
    def __init__(self, query: str):
        self._generator = iter(query)

    def dedup(self, *args, **kwargs) -> 'SPyLSearch':
        self._generator = _dedup(self._generator)
        return self

    def transaction(self, *args, **kwargs) -> 'SPyLSearch':
        pass

    def out(self):
        self._generator = _print(self._generator)
        return self

    def execute(self):
        for _result in self._generator:
            pass

    def results(self):
        yield from self._generator


SPyLSearch("querqy...")\
    .out()\
    .dedup()\
    .out()\
    .execute()
