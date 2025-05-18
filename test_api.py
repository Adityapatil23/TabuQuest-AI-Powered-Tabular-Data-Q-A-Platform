import requests, os, subprocess, time, sys, signal

BASE = "http://127.0.0.1:8000"

def _start_uvicorn():
    # launch server in a subprocess
    proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "app.main:app"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    time.sleep(1)  # give server a sec
    return proc

def test_filter_endpoint():
    proc = _start_uvicorn()
    try:
        r = requests.get(f"{BASE}/filter", params={"q": "age > 30"})
        assert r.status_code == 200
        assert r.json()["count"] == 3
    finally:
        proc.send_signal(signal.SIGINT)
