from pydantic import BaseModel, Field
from typing import List, Literal
from enum import Enum

class DecisionStatus(str, Enum):
    PROPOSED = "proposed"
    CONFIRMED = "confirmed"
    UNCLEAR = "unclear"

class RiskSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium" 
    HIGH = "high"

class Decision(BaseModel):
    decision: str = Field(description="The specific decision made or proposed")
    status: DecisionStatus = Field(description="Current status of the decision")
    evidence_quotes: List[str] = Field(description="Direct quotes from conversation supporting this decision")
    owner: str = Field(description="Person responsible for the decision or 'unknown'")
    deadline: str = Field(description="Timeline for implementation or 'unknown'")
    confidence: float = Field(ge=0.0, le=1.0, description="AI confidence in extraction accuracy")

class Assumption(BaseModel):
    assumption: str = Field(description="Key assumption being made")
    risk_if_wrong: str = Field(description="Potential impact if assumption proves incorrect")

class Risk(BaseModel):
    risk: str = Field(description="Identified risk or concern")
    severity: RiskSeverity = Field(description="Risk severity level")
    mitigation: str = Field(description="Suggested mitigation approach")

class DecisionAnalysis(BaseModel):
    decisions: List[Decision] = Field(description="Extracted decisions from conversation")
    assumptions: List[Assumption] = Field(description="Key assumptions identified")
    risks: List[Risk] = Field(description="Risks and concerns surfaced")
    open_questions: List[str] = Field(description="Unresolved questions requiring follow-up")
    human_must_decide: str = Field(description="Critical decision that requires human judgment")
    why_human: str = Field(description="Explanation of why this decision must remain human")
    scale_concerns: List[str] = Field(description="What would break first if scaling this process")
    
class HumanApproval(BaseModel):
    decision_index: int
    approved: bool
    edited_decision: str = ""
    human_confirmation: str = ""
