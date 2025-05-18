# TabuQuest – Demo

Tiny PoC showing an **NL→table filter**.

## Local run

```bash
python -m venv .venv && source .venv/bin/activate  # Win: .\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
