import os

from setuptools import setup

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="feedly-to-sqlite",
    description="Save data from feedly to a SQLite database",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Benjamin Congdon",
    author_email="me@bcon.gdn",
    url="https://github.com/bcongdon/feedly-to-sqlite",
    project_urls={
        "Source": "https://github.com/bcongdon/feedly-to-sqlite",
        "Issues": "https://github.com/bcongdon/feedly-to-sqlite/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Database",
    ],
    keywords="feedly sqlite export dogsheep",
    version=VERSION,
    packages=["feedly_to_sqlite"],
    entry_points="""
        [console_scripts]
        feedly-to-sqlite=feedly_to_sqlite.cli:cli
    """,
    install_requires=["click", "requests", "sqlite-utils~=1.11", "tqdm~=4.36"],
    extras_require={"test": ["pytest"]},
    tests_require=["feedly-to-sqlite[test]"],
)
