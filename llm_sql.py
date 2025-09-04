# llm_sql.py
import os, requests

# System prompt with a {user_query} placeholder
PROMPT = """
You are a helpful assistant that converts natural language questions into SQL queries.
Use the following PostgreSQL schema:

employees(id, name, department_id, email, salary)
departments(id, name)
orders(id, customer_name, employee_id, order_total, order_date)
products(id, name, price, embedding)

Rules:
- Only return a valid SQL query, nothing else.
- Do not include explanations or markdown.
- Always use lowercase table/column names.
- If the user asks for filters (like cheap, less than 1000), apply them in WHERE.

User query: {user_query}
SQL:
"""

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434/api/generate")  # ✅ default to standard Ollama port 11434
MODEL = os.getenv("OLLAMA_MODEL", "llama2")  # ✅ use a lighter default model

def generate_sql(user_query: str, prompt_template: str = PROMPT) -> str:
    prompt = prompt_template.replace("{user_query}", user_query)

    try:
        r = requests.post(
            OLLAMA_URL,
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=60
        )
        r.raise_for_status()
        text = r.json().get("response", "").strip()

        # Clean up result
        return text.split("```")[-1].strip() if "```" in text else text
    except Exception as e:
        raise RuntimeError(f"Ollama call failed: {e}")
