import re

toxic_words = [
    "idiot",
    "stupid",
    "hate",
    "noob",
    "trash",
    "shut up"
]

def detect_toxicity(message):
    text = message.lower()
    found_words = []

    for word in toxic_words:
        if re.search(r"\b" + re.escape(word) + r"\b", text):
            found_words.append(word)

    if found_words:
        return {
            "toxic": True,
            "words": found_words,
            "message": message
        }

    return {
        "toxic": False,
        "words": [],
        "message": message
    }