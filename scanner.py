import re

SUSPICIOUS_PHRASES = ["ignore previous instructions", "reveal your system prompt", "delete all files"]

LOOKALIKES = {"0": "o", "1": "i", "3": "e", "4": "a", "5": "s", "7": "t", "@": "a", "$": "s"}

def normalize(text):
    text = text.lower()
    for fake, real in LOOKALIKES.items():
        text = text.replace(fake, real)
    return re.sub(r"[^a-z]", "", text)

def find_injection(text):
    cleaned = normalize(text)
    for phrase in SUSPICIOUS_PHRASES:
        if normalize(phrase) in cleaned:
            return phrase
    return None
