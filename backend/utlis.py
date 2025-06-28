import re

def clean_text(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def split_into_chunks(text: str, max_words: int = 300) -> list:
    words = text.split()
    return [' '.join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

def title_case(text: str) -> str:
    return text.title()

def format_section_header(title: str) -> str:
    return f"\n\n===== {title.upper()} =====\n"
