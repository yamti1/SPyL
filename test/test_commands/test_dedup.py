from typing import Iterator, List, Set

import pytest
from nice_parametrize import parametrize

from spyl.commands import dedup


@parametrize(("generator", "fieldnames", "n", "keepempty", "expected_result_ids"), {
    "Single field, Default behavior": [
        [
            dict(id=1, first="a", last="z"),
            dict(id=2, first="A", last="Z"),
            dict(id=3, first="a", last="z"),
            dict(id=4, last="z"),
            dict(id=5, first=None, last="z"),
        ],
        ["first"], 1, False, [1, 2],
    ],
    "Multiple fields, Default behavior": [
        [
            dict(id=1, first="a", last="z"),
            dict(id=2, first="a", last="z"),
            dict(id=3, first="a", last="Z"),
            dict(id=4, first="A", last="Z"),
            dict(id=5, first="a", last="Z"),
        ],
        ["first", "last"], 1, False, [1, 3, 4],
    ],
    "Multiple fields, n > 1": [
        [
            dict(id=1, first="a", last="z"),
            dict(id=2, first="a", last="z"),
            dict(id=3, first="a", last="Z"),
            dict(id=4, first="A", last="Z"),
            dict(id=5, first="a", last="z"),
        ],
        ["first", "last"], 2, False, [1, 2, 3, 4],
    ],
    "Single field, keepempty = True": [
        [
            dict(id=1, first="a", last="z"),
            dict(id=2, last="z"),
            dict(id=3, first="a", last="Z"),
            dict(id=4, first=None, last="Z"),
            dict(id=5, first="a", last="z"),
            dict(id=6, first="A", last="z"),
            dict(id=7, first=None, last="Z"),
            dict(id=8, last="z"),
        ],
        ["first"], 1, True, [1, 2, 4, 6, 7, 8],
    ],
})
def test_sanity(generator: Iterator[dict], fieldnames: List[str], n: int, keepempty: bool,
                expected_result_ids: List[int]):
    results = dedup(generator, *fieldnames, n=n, keepempty=keepempty)
    for expected_result_id, result in zip(expected_result_ids, results):
        assert result["id"] == expected_result_id, f"Expected result with ID {expected_result_id}" \
                                                   f" but got {result} instead"
    try:
        extra_results = list(results)
    except StopIteration:
        pass
    else:
        assert not extra_results, f"Expected {len(expected_result_ids)} results, " \
                                  f"but got extra {len(extra_results)}: {extra_results}"


def test_non_positive_n_raises_value_error():
    with pytest.raises(ValueError):
        next(dedup(range(10), "a", n=0))

    with pytest.raises(ValueError):
        next(dedup(range(10), "a", n=-10))


def test_no_fieldnames_raises_value_error():
    with pytest.raises(ValueError):
        next(dedup(range(10)))
