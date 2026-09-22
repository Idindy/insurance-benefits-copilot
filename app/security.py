import re

def redact_pii(text: str) -> str:
    text = re.sub(r"\b[\w.+-]+@[\w.-]+\.\w+\b", "[EMAIL]", text)
    text = re.sub(r"\b\d{3}[-. ]?\d{2}[-. ]?\d{4}\b", "[SSN]", text)
    text = re.sub(r"\b(?:\+?1[-. ]?)?\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}\b", "[PHONE]", text)
    return text
