import os
import sys
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

# Add error handling for imports
try:
    from crew_runner import run_research_pipeline
except ImportError as e:
    print(f"Warning: crew_runner import failed: {e}")
    def run_research_pipeline(topic):
        return f"Mock report for {topic} - crew_runner not available"

try:
    from pdf_writer import save_report_as_pdf
except ImportError as e:
    print(f"Warning: pdf_writer import failed: {e}")
    def save_report_as_pdf(topic, text):
        return f"mock_report_{topic.replace(' ', '_')}.pdf"

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
def home():
    return {
        "message": "Thesis Assistant API is running!",
        "environment": os.getenv("RAILWAY_ENVIRONMENT", "development"),
        "python_version": sys.version
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

        report_text = run_research_pipeline(topic)

        print("\n===== FINAL GENERATED REPORT FOR DEBUGGING =====\n")
        print(report_text[:500] + "..." if len(report_text) > 500 else report_text)
        print("\n===== END OF REPORT =====\n")

        if not report_text or not report_text.strip():
            return {
                "message": "Report generation failed. No content was produced.",
                "report": "Failed to generate report content.",
                "filename": None
            }

        try:
            filename = save_report_as_pdf(topic, report_text)
            return {
                "message": "Report generated successfully",
                "report": report_text[:2000] + "..." if len(report_text) > 2000 else report_text,
                "filename": filename
            }
        except Exception as ve:
            print(f"PDF generation error: {ve}")
            return {
                "message": str(ve),
                "report": report_text[:2000] + "..." if len(report_text) > 2000 else report_text,
                "filename": None
            }
    except Exception as e:
        print(f"Research endpoint error: {e}")
        import traceback
        traceback.print_exc()
        return {
            "message": f"Error processing request: {str(e)}",
            "report": "Error processing request",
            "filename": None
        }

@app.get("/download/{filename}")
def download_file(filename: str):
    file_path = os.path.join("reports", filename)
    if os.path.exists(file_path):
        return FileResponse(
            path=file_path,
            filename=filename,
            media_type='application/pdf'
        )
    else:
        raise HTTPException(status_code=404, detail="File not found")

@app.get("/frontend")
def serve_frontend():
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