import os
from supabase import create_client
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Load env
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed(text: str):
    return model.encode(text, normalize_embeddings=True).tolist()

def search_products(query: str, top_k: int = 5, max_price: float = None):
    q_embedding = embed(query)

    params = {
        "query_embedding": q_embedding,
        "match_count": top_k
    }
    if max_price is not None:
        params["max_price"] = max_price

    result = supabase.rpc("match_products", params).execute()
    return result.data


if __name__ == "__main__":
    q = "wireless mouse"
    results = search_products(q, top_k=3)
    print("🔍 Query:", q)
    for r in results:
        print(f"- {r['name']} | Price: {r['price']}")
