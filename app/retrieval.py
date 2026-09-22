from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

DOCS = Path(__file__).resolve().parents[1] / "data" / "plans.txt"

class PlanIndex:
    def __init__(self):
        raw = DOCS.read_text().strip()
        self.chunks = [x.strip() for x in raw.split("\n\n") if x.strip()]
        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        self.matrix = self.vectorizer.fit_transform(self.chunks)

    def search(self, question: str, k: int = 3):
        q = self.vectorizer.transform([question])
        scores = cosine_similarity(q, self.matrix)[0]
        order = scores.argsort()[::-1][:k]
        return [{"text": self.chunks[i], "score": float(scores[i]), "source": f"plans.txt#chunk-{i+1}"} for i in order]
