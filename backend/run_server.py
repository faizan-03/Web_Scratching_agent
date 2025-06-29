import uvicorn
import webbrowser
import time
import threading
import os

def open_browser():
    time.sleep(2)
    # Only open browser in local development
    if os.getenv("RAILWAY_ENVIRONMENT") != "production":
        webbrowser.open("http://localhost:8000/frontend")

if __name__ == "__main__":
    print("Starting Thesis Research Assistant...")
    
    # Get port from environment (Railway sets this automatically)
    port = int(os.getenv("PORT", 8000))
    
    print(f"Backend API: http://0.0.0.0:{port}")
    print(f"Frontend UI: http://0.0.0.0:{port}/frontend")
    print(f"API Docs: http://0.0.0.0:{port}/docs")
    print("\nServer starting...")
    
    # Only start browser thread in local development
    if os.getenv("RAILWAY_ENVIRONMENT") != "production":
        threading.Thread(target=open_browser, daemon=True).start()
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",  # This is crucial for Railway
        port=port,
        reload=False  # Disable reload in production
    )
