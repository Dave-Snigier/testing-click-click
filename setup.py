from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="testing-click-click",
    description="null",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Dave Snigier",
    url="https://github.com/LambdaDriver/testing-click-click",
    project_urls={
        "Issues": "https://github.com/LambdaDriver/testing-click-click/issues",
        "CI": "https://github.com/LambdaDriver/testing-click-click/actions",
        "Changelog": "https://github.com/LambdaDriver/testing-click-click/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["testing_click_click"],
    entry_points="""
        [console_scripts]
        testing-click-click=testing_click_click.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    tests_require=["testing-click-click[test]"],
    python_requires=">=3.6",
)
