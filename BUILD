resource(name="setup", source="setup.py")

python_requirements(name="reqs", source="requirements.txt", resolve="main_resolve")

python_requirements(
    name="setuptoolsreqs",
    source="setuptools-requirements.txt",
    resolve="setuptools_resolve",
)


python_distribution(
    name="foodist",
    dependencies=[
        ":setup",
        "src/foo:foo",
        "src/foo:pyx",
        # Removing the below does not make any difference.
        "//:reqs",
    ],
    provides=python_artifact(
        name="foo",
        version="0.0.1",
    ),
    generate_setup=False,
)
