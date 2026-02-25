#!/usr/bin/env python3
"""
Main application launcher for AI Decision Boundary Assistant
"""

import sys
import os

def main():
    """Main application entry point"""
    # Add src to Python path
    src_path = os.path.join(os.path.dirname(__file__), 'src')
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
    
    # Import and run Streamlit
    try:
        from streamlit.web import cli
        
        # Set up Streamlit app path
        app_path = os.path.join(os.path.dirname(__file__), 'src', 'ai_decision_assistant', 'ui', 'app.py')
        
        # Run Streamlit app
        sys.argv = ["streamlit", "run", app_path, "--server.headless=true"]
        cli.main()
        
    except ImportError as e:
        print(f"❌ Error importing Streamlit: {e}")
        print("💡 Try installing with: pip install streamlit")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
