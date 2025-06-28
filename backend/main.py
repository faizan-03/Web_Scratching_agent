from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from crew_runner import run_research_pipeline
from pdf_writer import save_report_as_pdf
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TopicRequest(BaseModel):
    topic: str

@app.get("/")
def home():
    return {"message": "Thesis Assistant API is running!"}

@app.post("/research")
def research_topic(request: TopicRequest):
    topic = request.topic

    report_text = run_research_pipeline(topic)

    print("\n===== FINAL GENERATED REPORT FOR DEBUGGING =====\n")
    print(report_text)
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
    except ValueError as ve:
        print(ve)
        return {
            "message": str(ve),
            "report": "Error generating PDF report.",
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