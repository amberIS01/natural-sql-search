import os
from supabase import create_client
from sentence_transformers import SentenceTransformer
import numpy as np
from dotenv import load_dotenv

# Load env vars
load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")  # service role required
VECTOR_DIM = int(os.getenv("VECTOR_DIM", 384))

# Init clients
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed(text: str):
    """Generate embedding vector"""
    if not text:
        return None
    vec = model.encode(text, normalize_embeddings=True)  # ensures cosine works well
    return vec.tolist()

# Backfill products.name → products.embedding
def backfill_products():
    rows = supabase.table("products").select("id, name, embedding").execute().data
    for row in rows:
        if row["embedding"] is None:
            vec = embed(row["name"])
            supabase.table("products").update({"embedding": vec}).eq("id", row["id"]).execute()
            print(f"✅ Updated product {row['id']} - {row['name']}")

# Backfill employees.name → employees.name_embedding
def backfill_employees():
    rows = supabase.table("employees").select("id, name, name_embedding").execute().data
    for row in rows:
        if row["name_embedding"] is None:
            vec = embed(row["name"])
            supabase.table("employees").update({"name_embedding": vec}).eq("id", row["id"]).execute()
            print(f"✅ Updated employee {row['id']} - {row['name']}")

# Backfill orders.customer_name → orders.customer_embedding
def backfill_orders():
    rows = supabase.table("orders").select("id, customer_name, customer_embedding").execute().data
    for row in rows:
        if row["customer_embedding"] is None:
            vec = embed(row["customer_name"])
            supabase.table("orders").update({"customer_embedding": vec}).eq("id", row["id"]).execute()
            print(f"✅ Updated order {row['id']} - {row['customer_name']}")

if __name__ == "__main__":
    backfill_products()
    backfill_employees()
    backfill_orders()
    print("🎉 Backfilling done!")
