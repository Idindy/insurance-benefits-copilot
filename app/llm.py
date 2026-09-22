def grounded_answer(question: str, passages: list[dict]) -> str:
    """Deterministic demo answerer. Replace behind this interface with an approved LLM."""
    if not passages or passages[0]["score"] <= 0:
        return "I could not find that information in the indexed plan documents."
    return passages[0]["text"]
