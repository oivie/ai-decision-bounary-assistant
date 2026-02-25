"""
Example: Basic usage of AI Decision Boundary Assistant
"""

import sys
import os

# Add src to path for examples
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ai_decision_assistant.core.decision_analyzer import DecisionAnalyzer
from ai_decision_assistant.utils.helpers import format_confidence_score

def basic_analysis_example():
    """Basic conversation analysis example"""
    
    # Sample conversation thread
    conversation = """
    From: sarah.chen@fintech.com
    To: product-team@fintech.com
    Subject: Crypto Trading Feature - Decision Needed
    
    Team,
    
    We've been discussing the new crypto trading feature for weeks. 
    I think we need to make a decision today.
    
    My recommendation:
    - Launch with Bitcoin and Ethereum only
    - Set daily trading limits at $10,000 
    - Require additional KYC for crypto users
    - Go live in 2 weeks for Q2 targets
    
    Mike, can you handle the compliance review by Friday?
    Lisa, please prepare the user communications.
    
    The regulatory landscape is uncertain, but I believe the risk is manageable.
    
    Thoughts?
    
    Sarah
    """
    
    # Initialize analyzer
    print("🔍 Initializing AI Decision Analyzer...")
    analyzer = DecisionAnalyzer()
    
    # Analyze conversation
    print("📊 Analyzing conversation thread...")
    result = analyzer.analyze_conversation(conversation, high_stakes_mode=False)
    
    # Display results
    print("\n" + "="*60)
    print("📋 ANALYSIS RESULTS")
    print("="*60)
    
    print(f"\n🎯 DECISIONS IDENTIFIED ({len(result.decisions)} found):")
    for i, decision in enumerate(result.decisions, 1):
        confidence_display = format_confidence_score(decision.confidence)
        print(f"\n  {i}. {decision.decision}")
        print(f"     Status: {decision.status.value}")
        print(f"     Owner: {decision.owner}")
        print(f"     Deadline: {decision.deadline}")
        print(f"     Confidence: {confidence_display}")
        print(f"     Evidence: {decision.evidence_quotes[0][:50]}...")
    
    print(f"\n⚠️  RISKS IDENTIFIED ({len(result.risks)} found):")
    for risk in result.risks:
        severity_emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}
        emoji = severity_emoji.get(risk.severity.value, "⚫")
        print(f"  {emoji} {risk.risk}")
        print(f"     Mitigation: {risk.mitigation}")
    
    print(f"\n🤔 ASSUMPTIONS ({len(result.assumptions)} found):")
    for assumption in result.assumptions:
        print(f"  • {assumption.assumption}")
        print(f"    Risk: {assumption.risk_if_wrong}")
    
    print(f"\n❓ OPEN QUESTIONS ({len(result.open_questions)} found):")
    for question in result.open_questions:
        print(f"  • {question}")
    
    print(f"\n🚨 HUMAN BOUNDARY:")
    print(f"  Critical Decision: {result.human_must_decide}")
    print(f"  Why Human Required: {result.why_human}")
    
    print(f"\n📈 SCALE CONCERNS ({len(result.scale_concerns)} found):")
    for concern in result.scale_concerns:
        print(f"  • {concern}")
    
    return result

def high_stakes_example():
    """Example with high-stakes mode enabled"""
    
    conversation = """
    CONFIDENTIAL - Board Meeting Minutes Extract
    
    RE: Emergency Decision - Regulatory Investigation Response
    
    The CFTC has initiated a formal investigation into our crypto custody practices.
    We need to decide our response strategy immediately.
    
    Legal recommends full cooperation but minimal disclosure.
    We could face $50M+ in fines if this escalates.
    
    Options:
    1. Immediate voluntary compliance program
    2. Challenge the investigation scope  
    3. Settle preemptively
    
    This decision will impact our IPO timeline and customer trust.
    Board vote required by tomorrow.
    """
    
    print("\n" + "="*60)
    print("🚨 HIGH-STAKES MODE ANALYSIS")
    print("="*60)
    
    analyzer = DecisionAnalyzer()
    result = analyzer.analyze_conversation(conversation, high_stakes_mode=True)
    
    print(f"🎯 Critical Decision: {result.human_must_decide}")
    print(f"📊 Decisions Found: {len(result.decisions)} (all requiring human review)")
    print(f"⚠️  Risks Flagged: {len(result.risks)} (enhanced due to high-stakes)")
    
    return result

if __name__ == "__main__":
    print("AI Decision Boundary Assistant - Examples")
    print("=" * 50)
    
    # Run basic example
    result1 = basic_analysis_example()
    
    # Run high-stakes example  
    result2 = high_stakes_example()
    
    print(f"\n✅ Analysis complete! Found {len(result1.decisions)} decisions in basic mode")
    print(f"   and {len(result2.decisions)} decisions in high-stakes mode.")
