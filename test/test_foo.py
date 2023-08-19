from foo import bar


def test_foo():
    assert bar.mean([2.0, 4.0]) == 3.0
