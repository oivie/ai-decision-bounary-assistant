"""Utility functions for the AI Decision Boundary Assistant"""

import re
from datetime import datetime
from typing import List, Dict, Any
import streamlit as st

def format_confidence_score(confidence: float) -> str:
    """Format confidence score as percentage with color coding"""
    percentage = confidence * 100
    if confidence >= 0.8:
        return f"🟢 {percentage:.0f}%"
    elif confidence >= 0.5:
        return f"🟡 {percentage:.0f}%"
    else:
        return f"🔴 {percentage:.0f}%"

def clean_text(text: str) -> str:
    """Clean and normalize text input"""
    # Remove extra whitespace and normalize line endings
    text = re.sub(r'\s+', ' ', text.strip())
    return text

def extract_email_metadata(conversation: str) -> Dict[str, Any]:
    """Extract email headers and metadata from conversation"""
    metadata = {}
    
    # Look for common email patterns
    from_match = re.search(r'From:\s*(.+?)(?:\n|<)', conversation)
    if from_match:
        metadata['from'] = from_match.group(1).strip()
    
    to_match = re.search(r'To:\s*(.+?)(?:\n|$)', conversation)
    if to_match:
        metadata['to'] = to_match.group(1).strip()
    
    subject_match = re.search(r'Subject:\s*(.+?)(?:\n|$)', conversation)
    if subject_match:
        metadata['subject'] = subject_match.group(1).strip()
    
    return metadata

def generate_timestamp() -> str:
    """Generate current timestamp for logging"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def validate_decision_completeness(decisions: List[Dict[str, Any]], approvals: Dict[int, Any]) -> tuple[bool, List[str]]:
    """Validate that all decisions have required approvals"""
    errors = []
    
    for i, decision in enumerate(decisions):
        approval = approvals.get(i, {})
        
        if not approval.get('approved', False):
            errors.append(f"Decision {i+1} requires human approval")
        
        if decision.get('confidence', 0) < 0.3:
            errors.append(f"Decision {i+1} has very low confidence - review required")
    
    return len(errors) == 0, errors

def create_download_filename(prefix: str = "decision_log") -> str:
    """Create a timestamped filename for downloads"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.md"
