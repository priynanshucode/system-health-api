# System Health Monitor API

A small FastAPI application that reports CPU, memory, and disk usage for the machine running the API. It is a learning project, not a production monitoring service.

## Stack

Python, FastAPI, Uvicorn, and psutil. Exact dependencies are listed in `requirements.txt`.

## Run locally

```sh
git clone https://github.com/priynanshucode/system-health-api.git
cd system-health-api
python -m venv .venv
```

Activate the environment:

```sh
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

Install and start:

```sh
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Open [Swagger UI](http://127.0.0.1:8000/docs) or [ReDoc](http://127.0.0.1:8000/redoc).

## Endpoints

| Route | Response |
| --- | --- |
| `GET /` | Welcome message |
| `GET /health` | CPU, memory, and disk usage as percentages |

Example response (illustrative values):

```json
{
  "cpu_usage": 12.5,
  "memory_usage": 48.2,
  "disk_usage": 61.0
}
```

CPU is sampled over one second, so `/health` takes approximately one second to respond. Memory reflects virtual-memory utilization. Disk usage is measured at `os.path.abspath(os.sep)`, the root of the current drive on Windows or `/` on Unix-like systems.

## Scope

There is no authentication, persistent history, alerting, or remote-host monitoring. Keep this demo bound to localhost; it exposes host utilization metrics. It should not be treated as a production readiness or dependency-health check.

## Files

- `main.py` — application and routes
- `requirements.txt` — pinned dependencies
- `.gitignore` — local environment and cache exclusions
