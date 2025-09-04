import re

def parse_query(query: str):
    # Default values
    max_price = None
    clean_query = query

    # Look for patterns like "less than 1000", "under 2000"
    match = re.search(r"(?:less than|under)\s+(\d+)", query, re.IGNORECASE)
    if match:
        max_price = float(match.group(1))
        # Remove that part from the query so embedding is clean
        clean_query = re.sub(r"(?:less than|under)\s+\d+", "", query, flags=re.IGNORECASE).strip()

    return clean_query, max_price
