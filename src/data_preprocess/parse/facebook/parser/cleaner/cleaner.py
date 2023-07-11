import regex

def get_facebook_message_without_reactions(message: str) -> str:
    pattern = r'\p{So}\p{L}+\s\p{L}+'
    clean = regex.sub(pattern, "", message)
    return clean
