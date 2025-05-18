    from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from .engine import filter_df
import pandas as pd

app = FastAPI(title="TabuQuest Demo")

@app.get("/filter")
def filter_endpoint(q: Optional[str] = Query(None, description="NL filter")):
    if q is None or not q.strip():
        raise HTTPException(status_code=400, detail="Query string 'q' required")
    try:
        result: pd.DataFrame = filter_df(q)
    except Exception as ex:
        raise HTTPException(status_code=400, detail=str(ex))
    return {
        "columns": list(result.columns),
        "rows": result.to_dict(orient="records"),
        "count": len(result),
    }
