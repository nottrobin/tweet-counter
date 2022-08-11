# Packages
import regex
from tld import get_tld

# Twitter values
TWITTER_URL_SIZE = 23
TWITTER_SPECIAL_CHAR_SIZE = 2
TWITTER_STANDARD_CHAR_LIMIT = 0x2037
URL_MATCH = regex.compile(r"(?:https?:\/\/)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)")


def find_special_chars(text):
    """
    Find emoji and also other non-standard unicode characters.
    This uses Twitter's definition of "characters" that it uses
    for calculating tweet length, where emoji and all other
    unicode values above 0x2037 are considered to take up 2
    characters:
    https://developer.twitter.com/en/docs/counting-characters
    """

    special_chars = []

    for char in text:
        if (
            ord(char) > TWITTER_STANDARD_CHAR_LIMIT
        ):
            special_chars.append(char)

    return special_chars


def find_urls(text):
    """
    Find all URLs, including URLs without the "http://" scheme,
    from the text.
    But only include URLs with valid TLDs
    (e.g. yes example.tf, but not example.tx).

    This is attempting to follow twitter's definition of a URL,
    as used within its tweets:
    https://developer.twitter.com/en/docs/counting-characters
    """

    # Handle links
    urls = URL_MATCH.findall(text)

    # Check for real TLDs
    real_urls = []
    for url in urls:
        if get_tld(url, fix_protocol=True, fail_silently=True):
            real_urls.append(url)
    
    return real_urls


def count_tweet(tweet_text):
    # Remove URLs from text, keep separately
    urls = find_urls(tweet_text)
    for url in urls:
        tweet_text = tweet_text.replace(url, "")

    # Remove special characters from text, keep separately
    special_chars = find_special_chars(tweet_text)
    for char in special_chars:
        tweet_text = tweet_text.replace(char, "")

    # Calculate overall tweet length
    urls_length = len(urls) * TWITTER_URL_SIZE
    special_char_length = len(special_chars) * TWITTER_SPECIAL_CHAR_SIZE
    tweet_length = len(tweet_text) + urls_length + special_char_length

    return tweet_length

