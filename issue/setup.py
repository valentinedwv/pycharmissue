from setuptools import find_packages, setup

setup(
    name="issue",
    packages=find_packages(exclude=["issue_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
