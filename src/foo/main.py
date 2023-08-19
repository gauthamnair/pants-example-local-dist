from . import bar  # pants: no-infer-dep
import tabulate


def show() -> str:
    return tabulate.tabulate([["foo_mean", bar.mean([10.0, 20.0])]])