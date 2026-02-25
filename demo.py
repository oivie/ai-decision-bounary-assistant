#!/usr/bin/env python3
"""
Simple demo starter script that handles all the import setup automatically
"""

import os
import sys
import subprocess

def main():
    print("🚀 AI Decision Boundary Assistant - Demo Launcher")
    print("=" * 50)
    
    # Get project root directory
    project_root = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(project_root, 'src')
    
    print(f"📁 Project root: {project_root}")
    print(f"📦 Source path: {src_path}")
    
    # Check if required files exist
    app_path = os.path.join(src_path, 'ai_decision_assistant', 'ui', 'app.py')
    if not os.path.exists(app_path):
        print(f"❌ Error: App file not found at {app_path}")
        sys.exit(1)
    
    print("✅ All files found!")
    print("\n🌐 Starting Streamlit web interface...")
    print("📱 Visit: http://localhost:8501")
    print("🛑 Press Ctrl+C to stop")
    print("-" * 50)
    
    # Set environment and run Streamlit
    env = os.environ.copy()
    env['PYTHONPATH'] = src_path
    
    try:
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', app_path,
            '--server.port=8501',
            '--server.headless=true'
        ], env=env, cwd=project_root)
    except KeyboardInterrupt:
        print("\n👋 Demo stopped by user")
    except Exception as e:
        print(f"\n❌ Error running demo: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Install requirements: pip install -r requirements.txt")
        print("2. Check Python version: python3 --version (need 3.8+)")
        print("3. Try manual start: PYTHONPATH=src python3 -m streamlit run src/ai_decision_assistant/ui/app.py")

if __name__ == "__main__":
    main()
