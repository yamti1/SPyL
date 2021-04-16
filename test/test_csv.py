from spyl import Search, CSV


CSV_FILENAME = "./test/addresses.csv"


def tests_sanity():
    results = list(Search(
        CSV(CSV_FILENAME, fieldnames=("first_name", "last_name", "address", "city", "state", "code"))
    ).results())
    assert 6 == len(results)
