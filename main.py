# main.py
from fastapi import FastAPI
import psutil
import os

# Create the FastAPI application
app = FastAPI(title="System Health Monitor API")

# Default route
@app.get("/")
def root():
    return {"message": "Welcome to the System Health Monitor API"}

# /health route for system metrics
@app.get("/health")
def get_system_health():
    # Get CPU usage percentage
    cpu = psutil.cpu_percent(interval=1)
    
    # Get memory usage percentage
    memory = psutil.virtual_memory().percent

    # Get disk usage percentage (C drive on Windows)
    root_path = os.path.abspath(os.sep)
    disk = psutil.disk_usage(root_path).percent

    # Return JSON response
    return {
        "cpu_usage": cpu,
        "memory_usage": memory,
        "disk_usage": disk
    }
 
