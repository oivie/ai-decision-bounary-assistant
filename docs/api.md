# API Reference

## Core Classes

### DecisionAnalyzer

Main class for analyzing conversations and extracting decision information.

```python
from ai_decision_assistant.core.decision_analyzer import DecisionAnalyzer

analyzer = DecisionAnalyzer()
result = analyzer.analyze_conversation(conversation_text, high_stakes_mode=False)
```

#### Methods

- `analyze_conversation(conversation: str, high_stakes_mode: bool = False) -> DecisionAnalysis`
  - Analyzes conversation text and extracts structured decision information
  - Returns DecisionAnalysis object with decisions, risks, assumptions, etc.

- `generate_decision_log(analysis: DecisionAnalysis, approvals: Dict[int, Any]) -> str`
  - Generates formatted markdown decision log for export

### DecisionAnalysis

Pydantic model containing structured analysis results.

#### Properties
- `decisions: List[Decision]` - Extracted decisions with metadata
- `assumptions: List[Assumption]` - Key assumptions identified  
- `risks: List[Risk]` - Identified risks and concerns
- `open_questions: List[str]` - Unresolved questions
- `human_must_decide: str` - Critical decision requiring human judgment
- `why_human: str` - Explanation of why human decision is needed
- `scale_concerns: List[str]` - Potential scaling bottlenecks

### Decision

Individual decision extracted from conversation.

#### Properties
- `decision: str` - The specific decision text
- `status: DecisionStatus` - PROPOSED, CONFIRMED, or UNCLEAR
- `evidence_quotes: List[str]` - Supporting quotes from conversation
- `owner: str` - Person responsible (or "unknown")
- `deadline: str` - Timeline (or "unknown") 
- `confidence: float` - AI confidence score (0.0-1.0)

## Configuration

### Config Class

```python
from config.settings import Config

# Check if API key is configured
if Config.has_valid_api_key():
    # Use real AI analysis
else:
    # Use demo mode
```

## Utility Functions

### Helpers

```python
from ai_decision_assistant.utils.helpers import (
    format_confidence_score,
    clean_text,
    validate_decision_completeness
)

# Format confidence as colored percentage
display_text = format_confidence_score(0.85)  # "🟢 85%"

# Clean input text
clean = clean_text("  messy   text  ")  # "messy text"

# Validate approvals before export
is_valid, errors = validate_decision_completeness(decisions, approvals)
```

## Error Handling

```python
from ai_decision_assistant.utils.exceptions import (
    AnalysisError,
    ValidationError,
    APIError
)

try:
    result = analyzer.analyze_conversation(text)
except AnalysisError as e:
    # Handle analysis failure
    pass
except APIError as e:
    # Handle API issues
    pass
```
