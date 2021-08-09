# -*- coding: utf-8 -*-
import re

import setuptools

with open("CHANGELOG.md", "r") as fh:
    changelog = fh.read().splitlines()

raw_changelog_versions = [
    re.search(pattern=r"^##\s+version\s+(\d+\.\d+\.\d+)", string=c, flags=re.IGNORECASE)
    for c in changelog
]
changelog_version = [rcv for rcv in raw_changelog_versions if rcv is not None][0].group(
    1
)

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("dev-requirements.txt", "r") as fh:
    dev_requirements = fh.read().splitlines()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

requirements = [req for req in requirements if not req.lower().startswith("pytest")]

setuptools.setup(
    name="garden-of-things",
    version=changelog_version,
    author="frank690",
    author_email="sffresch@gmx.de",
    description="Supervise your garden with sensors and the internet in the garden-of-things",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frank690/garden-of-things",
    packages=setuptools.find_packages(
        exclude=["tests", "tests.*", "*.tests.*", "*.tests", "docs"]
    ),
    include_package_data=True,
    setup_requires=["cython"],
    install_requires=requirements,
    test_suite="tests",
    extras_require={
        "dev": dev_requirements,
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Microsoft :: Windows ",
        "Operating System :: Unix",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.7",
)
