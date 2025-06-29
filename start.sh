#!/bin/bash
echo "Starting Thesis Research Assistant..."
cd backend
echo "Current directory: $(pwd)"
echo "Files in directory: $(ls -la)"
echo "Starting uvicorn server..."
uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000} --log-level info
