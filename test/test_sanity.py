from typing import List

from nice_parametrize import parametrize

from spyl import Search, CSV

CSV_FILENAME = "./test/addresses.csv"


def test_search():
    search = Search(range(3))
    assert list(search.results()) == [0, 1, 2]


def test_csv():
    results = list(Search(
        CSV(CSV_FILENAME, fieldnames=("first_name", "last_name", "address", "city", "state", "code"))
    ).results())
    assert len(results) == 6, "Unexpected number of results"
    for result in results:
        assert len(result) == 6, f"Unexpected number of fields in result: {result}"


@parametrize(["search", "expected_results"], {
    "Dedup": [
        Search([
            dict(id=1, foo="bar"),
            dict(id=1, foo="jar"),
            dict(id=2, foo="tar"),
        ]).dedup("id"),
        [
            dict(id=1, foo="bar"),
            dict(id=2, foo="tar"),
        ]
    ]
})
def test_search_examples(search: Search, expected_results: List[dict]):
    for expected_result, actual_result in zip(search.results(), expected_results):
        assert expected_result == actual_result, "Search returned an unexpected result"
