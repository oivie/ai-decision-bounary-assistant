#!/bin/bash

# Simple launcher script for AI Decision Boundary Assistant

echo "🚀 Starting AI Decision Boundary Assistant Demo..."

# Set Python path to include src directory
export PYTHONPATH="$(pwd)/src:$PYTHONPATH"

# Launch Streamlit app using python module
echo "📡 Launching web interface..."
python3 -m streamlit run src/ai_decision_assistant/ui/app.py --server.port=8501 --server.headless=true

echo "✅ Demo launched! Visit: http://localhost:8501"
