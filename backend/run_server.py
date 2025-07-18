import uvicorn
import webbrowser
import time
import threading
import os
import sys

def open_browser():
    time.sleep(2)
    # Only open browser in local development
    if os.getenv("RAILWAY_ENVIRONMENT") != "production":
        webbrowser.open("http://localhost:8000/frontend")

if __name__ == "__main__":
    try:
        print("Starting Thesis Research Assistant...")
        
        # Get port from environment (Railway sets this automatically)
        port = int(os.getenv("PORT", 8000))
        
        print(f"Environment: {os.getenv('RAILWAY_ENVIRONMENT', 'development')}")
        print(f"Port: {port}")
        print(f"Python version: {sys.version}")
        print(f"Current working directory: {os.getcwd()}")
        print(f"Files in current directory: {os.listdir('.')}")
        
        # Check if main.py exists
        if not os.path.exists("main.py"):
            print("ERROR: main.py not found in current directory!")
            sys.exit(1)
        
        print(f"Backend API: http://0.0.0.0:{port}")
        print(f"Frontend UI: http://0.0.0.0:{port}/frontend")
        print(f"API Docs: http://0.0.0.0:{port}/docs")
        print("\nServer starting...")
        
        # Only start browser thread in local development
        if os.getenv("RAILWAY_ENVIRONMENT") != "production":
            threading.Thread(target=open_browser, daemon=True).start()
        
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=port,
            reload=False,
            log_level="info"
        )
        
    except Exception as e:
        print(f"ERROR starting server: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
