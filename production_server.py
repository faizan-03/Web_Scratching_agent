#!/usr/bin/env python3
import os
import sys
import uvicorn

# Add the backend directory to Python path
backend_path = os.path.join(os.path.dirname(__file__), 'backend')
sys.path.insert(0, backend_path)

def main():
    port = int(os.getenv("PORT", 8000))
    print(f"Starting Thesis Assistant API on port {port}")
    print(f"Environment: {os.getenv('RAILWAY_ENVIRONMENT', 'development')}")
    print(f"Python path: {sys.path}")
    print(f"Current directory: {os.getcwd()}")
    print(f"Backend path: {backend_path}")
    
    # Change to backend directory
    os.chdir(backend_path)
    print(f"Changed to directory: {os.getcwd()}")
    print(f"Files in backend: {os.listdir('.')}")
    
    try:
        uvicorn.run(
            "main_simple:app",  # Use simple version first
            host="0.0.0.0",
            port=port,
            log_level="info",
            reload=False
        )
    except Exception as e:
        print(f"Error starting server: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
