from spyl import Search


def test_sanity():
    search = Search(range(3))
    assert [0, 1, 2] == list(search.results())


