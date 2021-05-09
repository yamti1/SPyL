from typing import Iterator


def dedup(generator: Iterator[dict], *fieldnames: str, n: int = 1, keepempty: bool = False):
    if not n > 0:
        raise ValueError("`dedup` expects n > 0")
    if not fieldnames:
        raise ValueError("`dedup` expects at least one field name")

    d = {}  # Maps tuples of encountered value-combinations to the number of times the combination appeared
    for result in generator:
        values = tuple(result.get(fieldname) for fieldname in fieldnames)
        if None in values:
            if keepempty:
                yield result
            continue
        encountered_count = d.setdefault(values, 0)
        if encountered_count >= n:
            continue
        d[values] += 1
        yield result


def print_gen(generator):
    for event in generator:
        print(event)
        yield event
