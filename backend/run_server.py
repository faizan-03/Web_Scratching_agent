import uvicorn
import webbrowser
import time
import threading

def open_browser():
    time.sleep(2)
    webbrowser.open("http://localhost:8000/frontend")

if __name__ == "__main__":
    print("Starting Thesis Research Assistant...")
    print("Backend API: http://localhost:8000")
    print("Frontend UI: http://localhost:8000/frontend")
    print("API Docs: http://localhost:8000/docs")
    print("\nServer starting...")
    
    threading.Thread(target=open_browser, daemon=True).start()
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
