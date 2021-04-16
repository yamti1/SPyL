from spyl import Search, UserSource


def test_sanity():
    search = Search(range(3))
    assert [0, 1, 2] == list(search.results())


