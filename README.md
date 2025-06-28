# 🎓 Thesis Research Assistant

An AI-powered research assistant that generates comprehensive thesis reports with beautiful PDF formatting.

## 🚀 Quick Start

### Option 1: Simple Startup (Windows)
```bash
# Double-click the batch file
start_app.bat
```

### Option 2: Manual Startup
```bash
# Navigate to backend directory
cd backend

# Start the server
python run_server.py
```

### Option 3: Using uvicorn directly
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 🌐 Access Points

- **Frontend UI**: http://localhost:8000/frontend
- **API Root**: http://localhost:8000/
- **API Documentation**: http://localhost:8000/docs
- **Download PDFs**: http://localhost:8000/download/{filename}

## 🔧 API Endpoints

### POST /research
Generate a research report
```json
{
  "topic": "Your research topic"
}
```

**Response:**
```json
{
  "message": "✅ Report generated successfully",
  "report": "Preview of the generated report...",
  "filename": "report_filename.pdf"
}
```

### GET /download/{filename}
Download generated PDF reports

### GET /frontend
Serve the web interface

### GET /static/{file_path}
Serve static files (CSS, JS)

## 🎨 Features

### Frontend
- ✅ Modern, responsive UI
- ✅ Real-time loading indicators
- ✅ Error handling and user feedback
- ✅ Direct PDF download
- ✅ Enter key support

### Backend
- ✅ FastAPI with automatic documentation
- ✅ CORS enabled for frontend integration
- ✅ Enhanced PDF generation with blue theme
- ✅ Robust error handling
- ✅ File serving capabilities

### PDF Reports
- ✅ Professional blue color scheme
- ✅ Elegant borders and layouts
- ✅ Table of contents with links
- ✅ Enhanced typography (Times New Roman)
- ✅ Automatic section detection
- ✅ Unicode character support

## 🛠️ Testing

```bash
# Test API connection
python test_connection.py

# Test PDF generation
python test_enhanced_pdf.py
```

## 📁 Project Structure

```
scraping_agent/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── pdf_writer.py        # Enhanced PDF generation
│   ├── crew_runner.py       # Research pipeline
│   ├── run_server.py        # Server startup script
│   └── agents/              # AI agents
├── frontend/
│   ├── index.html           # Web interface
│   ├── script.js            # Frontend logic
│   └── style.css            # Styling
├── reports/                 # Generated PDF reports
├── assets/                  # Logo and images
└── start_app.bat           # Windows startup script
```

## 🔧 Configuration

The application runs on `localhost:8000` by default. To change:

1. Update `run_server.py` port
2. Update frontend JavaScript API URLs
3. Update HTML static file URLs

## 🐛 Troubleshooting

### Server won't start
- Check if port 8000 is available
- Ensure all dependencies are installed
- Check Python path and virtual environment

### Frontend not loading
- Verify server is running on correct port
- Check browser console for errors
- Ensure static files are accessible

### PDF generation fails
- Check research pipeline is working
- Verify PDF dependencies are installed
- Check file permissions for reports directory

## 📝 Usage

1. Start the server using any method above
2. Open http://localhost:8000/frontend in your browser
3. Enter a research topic
4. Click "Start Research" or press Enter
5. Wait for processing (this may take a few minutes)
6. Download the generated PDF report

Enjoy your AI-powered research assistant! 🎉
