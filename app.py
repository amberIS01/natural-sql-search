import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

import streamlit as st
from vector_search import search_products
from query_parser import parse_query
from llm_sql import generate_sql, PROMPT   # ✅ import PROMPT too
from sql_guard import validate_sql
from run_sql import run_sql   # new helper to connect to Postgres directly

st.title("🔍 Natural Language Search Demo")

# Choose mode
mode = st.radio("Select Search Mode:", ["Semantic Product Search", "Structured DB Search"])

if mode == "Semantic Product Search":
    query = st.text_input("Enter your search query:")
    if st.button("Search") and query.strip():
        with st.spinner("Searching products..."):
            clean_query, max_price = parse_query(query)
            results = search_products(clean_query, top_k=5, max_price=max_price)

        if results:
            st.subheader("Results:")
            for r in results:
                st.write(f"**{r['name']}** — 💲{r['price']} (similarity: {round(r['similarity'], 3)})")
        else:
            st.info("No matching products found.")

else:
    query = st.text_input("Ask a question (employees, departments, orders):")
    if st.button("Run SQL") and query.strip():
        with st.spinner("Generating SQL with LLM..."):
            # ✅ pass PROMPT explicitly
            raw_sql = generate_sql(query, PROMPT)

        try:
            safe_sql = validate_sql(raw_sql)
            rows = run_sql(safe_sql)

            st.subheader("Generated SQL")
            st.code(safe_sql, language="sql")

            st.subheader("Results")
            st.dataframe(rows)

        except Exception as e:
            st.error(f"❌ Query blocked or failed: {e}")
