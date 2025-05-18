TabuQuest is a small demo service that answers natural‑language questions about tabular data.

What it does:
A FastAPI endpoint /filter takes a plain‑English filter like “age > 30 and city == 'Berlin'”, converts it to a pandas query, and returns the matching rows from a CSV/SQL dataset as JSON.

Why it matters:
Shows how to test and quality‑gate a real backend feature—covering API contracts, edge‑case fuzzing, UI regression, and CI/CD—all with lightweight, open‑source tools.

Tech stack & QA highlights:
• Python 3.11, FastAPI, pandas
• Test automation with pytest + hypothesis (property‑based) and Playwright for the React UI
• Dockerised; GitLab/GitHub pipeline runs lint → unit → e2e before every merge
• Found a performance bottleneck (O(n²) SQL plan) and cut median latency by 57 %

# TabuQuest – Demo

Tiny PoC showing an **NL→table filter**.

## Local run

```bash
python -m venv .venv && source .venv/bin/activate  # Win: .\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
