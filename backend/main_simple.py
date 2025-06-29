import os
import sys
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(title="Thesis Assistant API", version="1.0.0")

# Update CORS for production
is_production = os.getenv("RAILWAY_ENVIRONMENT") == "production"
origins = ["*"] if is_production else ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TopicRequest(BaseModel):
    topic: str

@app.get("/")
def home(request: Request):
    # Check if this is a browser request (Accept header contains text/html)
    accept_header = request.headers.get("accept", "")
    
    if "text/html" in accept_header:
        # Browser request - serve frontend
        frontend_path = os.path.join("..", "frontend", "index.html")
        if os.path.exists(frontend_path):
            return FileResponse(frontend_path)
        else:
            raise HTTPException(status_code=404, detail="Frontend not found")
    else:
        # API request - return JSON
        return {
            "message": "Thesis Assistant API is running!",
            "environment": os.getenv("RAILWAY_ENVIRONMENT", "development"),
            "python_version": sys.version,
            "status": "Production Ready",
            "endpoints": {
                "api_info": "/api",
                "health": "/health", 
                "research": "/research",
                "frontend": "/ (browser) or /frontend"
            }
        }

@app.get("/api")
def api_info():
    return {
        "message": "Thesis Assistant API is running!",
        "environment": os.getenv("RAILWAY_ENVIRONMENT", "development"),
        "python_version": sys.version,
        "status": "Production Ready"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy", 
        "message": "Thesis Assistant API is running!",
        "environment": os.getenv("RAILWAY_ENVIRONMENT", "development")
    }

@app.post("/research")
def research_topic(request: TopicRequest):
    try:
        topic = request.topic
        print(f"Processing research request for topic: {topic}")

        # Mock response for now - will work without complex dependencies
        mock_report = f"""
        # Research Report: {topic}
        
        This is a mock research report generated for the topic: {topic}
        
        ## Executive Summary
        This report provides comprehensive analysis of {topic} based on current research and data.
        
        ## Key Findings
        1. Topic analysis shows significant relevance in current market
        2. Multiple research sources confirm importance of {topic}
        3. Recommendations for future research directions
        
        ## Conclusion
        The research on {topic} indicates promising opportunities for further investigation.
        
        Note: This is a demonstration version. Full research capabilities will be restored once all dependencies are properly configured.
        """

        return {
            "message": "Report generated successfully (Demo Mode)",
            "report": mock_report,
            "filename": f"demo_report_{topic.replace(' ', '_')}.pdf"
        }
        
    except Exception as e:
        print(f"Research endpoint error: {e}")
        return {
            "message": f"Error processing request: {str(e)}",
            "report": "Error processing request",
            "filename": None
        }

@app.get("/download/{filename}")
def download_file(filename: str):
    # Mock download for now
    raise HTTPException(status_code=404, detail="Download feature temporarily disabled in demo mode")

@app.get("/frontend")
def serve_frontend():
    # Redirect to root since frontend is now served at /
    frontend_path = os.path.join("..", "frontend", "index.html")
    if os.path.exists(frontend_path):
        return FileResponse(frontend_path)
    else:
        raise HTTPException(status_code=404, detail="Frontend not found")

@app.get("/static/{file_path:path}")
def serve_static(file_path: str):
    static_path = os.path.join("..", "frontend", file_path)
    if os.path.exists(static_path):
        return FileResponse(static_path)
    else:
        raise HTTPException(status_code=404, detail="Static file not found")

@app.get("/assets/{file_path:path}")
def serve_assets(file_path: str):
    asset_path = os.path.join("..", "assets", file_path)
    if os.path.exists(asset_path):
        return FileResponse(asset_path)
    else:
        raise HTTPException(status_code=404, detail="Asset file not found")
