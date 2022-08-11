from tweet_counter import count_tweet

tweet_text = (
    "Otters 👪 otters 𝗼𝘁𝘁𝗲𝗿𝘀 otters otters.otters otters.com/otters otters "
    "otters http://otters otters https://otters.uk otters otters.com otters "
    "otters otters otters ótters Ótters òttérs otters otters otters otters "
    "otters.​biz otters otters otters otter"
)

size = count_tweet(tweet_text)

print(f"Tweet text: { tweet_text }")
print(f"Tweet size: { size }")

assert size == 280

print("Test passed!")
