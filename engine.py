from pathlib import Path
import pandas as pd
import re

DATA_PATH = Path(__file__).parent.parent / "data" / "sample.csv"
DF = pd.read_csv(DATA_PATH)


def nl_to_query(nl: str) -> str:
    """
    Convert a tiny subset of NL filters to pandas query.
    Examples:
        "age > 30"
        "city == 'London'"
        "salary >= 50000 and age < 40"
    """
    # extremely naive — just ensure allowed tokens
    allowed_cols = {"age", "city", "salary", "name"}
    col_pattern = r"\b(" + "|".join(allowed_cols) + r")\b"
    if not re.fullmatch(r"[A-Za-z0-9 _><=!'\"&|]+", nl):
        raise ValueError("Unsafe characters in query")
    if not re.search(col_pattern, nl):
        raise ValueError("Unknown column")
    return nl


def filter_df(nl: str) -> pd.DataFrame:
    query = nl_to_query(nl)
    return DF.query(query)
