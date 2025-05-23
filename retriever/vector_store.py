# -----------------------------
import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

class VectorStore:
    def __init__(self):
        self.index = faiss.IndexFlatL2(384)
        self.texts = []

    def add(self, documents):
        embeddings = model.encode(documents)
        self.index.add(embeddings)
        self.texts.extend(documents)

    def search(self, query, top_k=3):
        q_embed = model.encode([query])
        D, I = self.index.search(q_embed, top_k)
        return [self.texts[i] for i in I[0]]

store = VectorStore()
store.add(["TSMC earnings beat expectations.", "Samsung earnings missed target."])