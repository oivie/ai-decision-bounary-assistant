#!/usr/bin/env python3
"""
Command-line interface for AI Decision Boundary Assistant
"""

import argparse
import sys
import os
from pathlib import Path

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from ai_decision_assistant.core.decision_analyzer import DecisionAnalyzer
from ai_decision_assistant.utils.helpers import format_confidence_score


def analyze_file(file_path: str, high_stakes: bool = False, output_file: str = None):
    """Analyze a conversation from a file"""
    
    if not os.path.exists(file_path):
        print(f"❌ Error: File '{file_path}' not found")
        sys.exit(1)
    
    # Read conversation
    with open(file_path, 'r', encoding='utf-8') as f:
        conversation = f.read()
    
    # Analyze
    print(f"🔍 Analyzing conversation from '{file_path}'...")
    analyzer = DecisionAnalyzer()
    result = analyzer.analyze_conversation(conversation, high_stakes)
    
    # Display results
    print(f"\n📊 Analysis Results:")
    print(f"   Decisions: {len(result.decisions)}")
    print(f"   Risks: {len(result.risks)}")
    print(f"   Assumptions: {len(result.assumptions)}")
    print(f"   Open Questions: {len(result.open_questions)}")
    print(f"   Critical Decision: {result.human_must_decide}")
    
    # Export if requested
    if output_file:
        log_content = analyzer.generate_decision_log(result, {})
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(log_content)
        print(f"📄 Decision log exported to '{output_file}'")
    
    return result


def analyze_text(text: str, high_stakes: bool = False):
    """Analyze conversation text directly"""
    
    print("🔍 Analyzing provided text...")
    analyzer = DecisionAnalyzer()
    result = analyzer.analyze_conversation(text, high_stakes)
    
    # Display detailed results
    print(f"\n🎯 DECISIONS ({len(result.decisions)} found):")
    for i, decision in enumerate(result.decisions, 1):
        confidence = format_confidence_score(decision.confidence)
        print(f"  {i}. {decision.decision}")
        print(f"     Status: {decision.status.value}")
        print(f"     Owner: {decision.owner}")
        print(f"     Confidence: {confidence}")
        print()
    
    print(f"🚨 CRITICAL DECISION: {result.human_must_decide}")
    print(f"💭 RATIONALE: {result.why_human}")
    
    return result


def main():
    """Main CLI entry point"""
    
    parser = argparse.ArgumentParser(
        description="AI Decision Boundary Assistant - Command Line Interface",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --gui                           # Launch web interface
  %(prog)s --text "Meeting notes..."       # Analyze text directly  
  %(prog)s --file conversation.txt         # Analyze file
  %(prog)s --file notes.txt --high-stakes # High-stakes analysis
  %(prog)s --file notes.txt --output log.md # Export decision log
        """
    )
    
    # Input options (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument('--gui', action='store_true', 
                           help='Launch web interface')
    input_group.add_argument('--text', type=str,
                           help='Conversation text to analyze')
    input_group.add_argument('--file', type=str,
                           help='File containing conversation to analyze')
    
    # Analysis options
    parser.add_argument('--high-stakes', action='store_true',
                       help='Enable high-stakes mode for conservative analysis')
    parser.add_argument('--output', '-o', type=str,
                       help='Export decision log to file')
    
    args = parser.parse_args()
    
    try:
        if args.gui:
            # Launch Streamlit GUI
            print("🚀 Launching AI Decision Boundary Assistant...")
            import streamlit.web.cli as stcli
            import sys
            
            app_path = os.path.join(os.path.dirname(__file__), 'src', 'ai_decision_assistant', 'ui', 'app.py')
            sys.argv = ["streamlit", "run", app_path]
            stcli.main()
            
        elif args.text:
            # Analyze provided text
            analyze_text(args.text, args.high_stakes)
            
        elif args.file:
            # Analyze file
            analyze_file(args.file, args.high_stakes, args.output)
            
    except KeyboardInterrupt:
        print("\n👋 Analysis interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
