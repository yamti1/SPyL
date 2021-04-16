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
