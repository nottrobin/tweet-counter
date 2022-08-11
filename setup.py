#! /usr/bin/env python3

# Packages
from setuptools import setup

setup(
    name="tweet-counter",
    version="0.1.0",
    author="Robin Winslow",
    author_email="robin@robinwinslow.co.uk",
    url="https://github.com/nottrobin/tweet-counter",
    description=(
        "Calculate the length that Twitter will consider a Tweet to be"
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=["tweet_counter"],
    install_requires=[
        "regex>=2022.7.25",
        "tld>=0.12.6",
    ],
    scripts=[
        "count-tweet",
    ],
)
