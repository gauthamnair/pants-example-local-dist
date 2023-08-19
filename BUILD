resource(name="readme", source="README.md")
resources(name="setup", sources=["setup.*"])


python_requirements(name="setuptoolsreqs",
                    source="setuptools-requirements.txt",
                    resolve="setuptools_resolve")


python_distribution(
    name="foodist",
    dependencies=[":setup",
                  "src/foo:foo",
                  "src/foo:pyx",
                  ],
    provides=python_artifact(
        name="foo",
        version="0.0.1",
    ),
    generate_setup = False
)