from foo.bar import main  # pants: no-infer-dep


def test_show():
    expected = '--------  --\nfoo_mean  15\n--------  --'
    assert main.show() == expected
