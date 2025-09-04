
# 🔍 Natural Language Search Demo

This project demonstrates **two powerful ways** of searching data:

1. **Semantic Product Search** – Finds similar products using vector embeddings stored in Supabase.
2. **Structured DB Search** – Converts natural language into SQL queries using a local LLM (Ollama + Mistral).

---


## 📂 Project Structure

```
.
├── app.py              # Streamlit UI
├── query_parser.py     # Extract filters like price
├── vector_search.py    # Embedding + Supabase vector similarity
├── llm_sql.py          # LLM prompt + SQL generation
├── sql_guard.py        # Validate SQL before execution
├── run_sql.py          # Run queries on Postgres
├── requirements.txt    # Python dependencies
└── .env                # Secrets (ignored in Git)
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/nl-search-demo.git
cd nl-search-demo
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Supabase

- Create a **Supabase project** → note the `URL` and `ANON_KEY`.
- Create tables:

  - `products(id, name, price, embedding)`
  - `employees(id, name, department_id, email, salary)`
  - `departments(id, name)`
  - `orders(id, customer_name, employee_id, order_total, order_date)`
- Load product embeddings (you can generate with OpenAI or local embedding model).

### 5️⃣ Setup Ollama (for SQL generation)

Install Ollama and pull the Mistral model:

```bash
curl -fsSL https://ollama.com/install.sh | sh   # Mac/Linux
# Windows → https://ollama.com/download

ollama pull mistral
```

### 6️⃣ Configure environment variables

Create a `.env` file:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
OLLAMA_URL=http://127.0.0.1:11434/api/generate
OLLAMA_MODEL=mistral
```

---

## 🚀 Run the App

```bash
streamlit run app.py
```

Now open 👉 [http://localhost:8501](http://localhost:8501)

---

## 🛠️ Features

✅ **Semantic Product Search**

- Extracts filters like *“less than 1000”*
- Uses Supabase vector similarity search
- Returns top-k matches with similarity score

✅ **Structured DB Search**

- Converts English → SQL with **Mistral LLM**
- SQL is validated by `sql_guard.py`
- Results displayed as dataframe

---

## 📊 Example Queries

### Semantic Search

- `cheap wireless accessories less than 1000`
- `gaming keyboard`
- `bluetooth headphones under 2000`

### Structured Search

- `list all employees in the sales department`
- `show top 5 highest paid employees`
- `find orders placed after Jan 2024`

---

## ⚠️ Notes

- `.env` file is ignored (check `.gitignore`).
- Do not commit Supabase keys.
- Ollama models can be large (4–7 GB).

---

## 📜 License

MIT License – free to use and modify.

<style>#mermaid-1756957193042{font-family:sans-serif;font-size:16px;fill:#333;}#mermaid-1756957193042 .error-icon{fill:#552222;}#mermaid-1756957193042 .error-text{fill:#552222;stroke:#552222;}#mermaid-1756957193042 .edge-thickness-normal{stroke-width:2px;}#mermaid-1756957193042 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1756957193042 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1756957193042 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1756957193042 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1756957193042 .marker{fill:#333333;}#mermaid-1756957193042 .marker.cross{stroke:#333333;}#mermaid-1756957193042 svg{font-family:sans-serif;font-size:16px;}#mermaid-1756957193042 .label{font-family:sans-serif;color:#333;}#mermaid-1756957193042 .label text{fill:#333;}#mermaid-1756957193042 .node rect,#mermaid-1756957193042 .node circle,#mermaid-1756957193042 .node ellipse,#mermaid-1756957193042 .node polygon,#mermaid-1756957193042 .node path{fill:#ECECFF;stroke:#9370DB;stroke-width:1px;}#mermaid-1756957193042 .node .label{text-align:center;}#mermaid-1756957193042 .node.clickable{cursor:pointer;}#mermaid-1756957193042 .arrowheadPath{fill:#333333;}#mermaid-1756957193042 .edgePath .path{stroke:#333333;stroke-width:1.5px;}#mermaid-1756957193042 .flowchart-link{stroke:#333333;fill:none;}#mermaid-1756957193042 .edgeLabel{background-color:#e8e8e8;text-align:center;}#mermaid-1756957193042 .edgeLabel rect{opacity:0.5;background-color:#e8e8e8;fill:#e8e8e8;}#mermaid-1756957193042 .cluster rect{fill:#ffffde;stroke:#aaaa33;stroke-width:1px;}#mermaid-1756957193042 .cluster text{fill:#333;}#mermaid-1756957193042 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:sans-serif;font-size:12px;background:hsl(80,100%,96.2745098039%);border:1px solid #aaaa33;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1756957193042:root{--mermaid-font-family:sans-serif;}#mermaid-1756957193042:root{--mermaid-alt-font-family:sans-serif;}#mermaid-1756957193042 flowchart-v2{fill:apa;}</style>
