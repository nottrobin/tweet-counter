# Tweet counter

[![PyPI version](https://badge.fury.io/py/tweet-counter.svg)](https://pypi.org/project/tweet-counter/)

Calculate the size that Twitter [will consider a tweet to be](https://developer.twitter.com/en/docs/counting-characters).

This is not as advanced as [the official twitter-text libraries](/home/robin/projects/twitter-counter/README.md), but attempts to at least take into account the following:

- Twitter will convert anything that looks like a URL (with a [valid TLD](https://data.iana.org/TLD/tlds-alpha-by-domain.txt)) into a Twitter short link, and count it as taking up exactly 23 characters
- Twitter counts emoji and any unicode character above `U+2037` as each taking up 2 characters

## Installation

``` bash
pip3 install tweet-counter
```

## Python usage

``` python
from tweet_counter import count_tweet

print(count_tweet("Otters 👪 otters 𝗼𝘁𝘁𝗲𝗿𝘀 otters otters.com/otters"))
# Output => 60
```

## Command-line usage

``` bash
$ count-tweet "Otters 👪 otters 𝗼𝘁𝘁𝗲𝗿𝘀 otters otters.com/otters"
60
```
