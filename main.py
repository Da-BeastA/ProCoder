import subprocess
import time

# Start the FastAPI server
backend_process = subprocess.Popen(["uvicorn", "backend.api.server:app", "--host", "0.0.0.0", "--port", "8000"])

# Wait for the backend to start
time.sleep(3)

# Start the Streamlit app
frontend_process = subprocess.Popen(["streamlit", "run", "app.py"])

# Keep the script running
try:
    backend_process.wait()
    frontend_process.wait()
except KeyboardInterrupt:
    print("Shutting down processes...")
    backend_process.terminate()
    frontend_process.terminate()
