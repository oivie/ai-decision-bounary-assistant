import json
import openai
from typing import Dict, Any
import sys
import os
from dotenv import load_dotenv

# Add src to Python path for absolute imports
current_file = os.path.abspath(__file__)
core_dir = os.path.dirname(current_file)
ai_decision_assistant_dir = os.path.dirname(core_dir)
src_dir = os.path.dirname(ai_decision_assistant_dir)

if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from ai_decision_assistant.core.models import DecisionAnalysis

load_dotenv()

class DecisionAnalyzer:
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key or api_key == 'your-openai-key-here':
            # Create a mock client for demo purposes
            self.client = None
        else:
            try:
                self.client = openai.OpenAI(api_key=api_key)
            except Exception as e:
                print(f"⚠️  OpenAI client initialization failed: {e}")
                print("🔧 Falling back to demo mode...")
                self.client = None
        
    def get_system_prompt(self, high_stakes_mode: bool = False) -> str:
        base_prompt = """You are a Decision Intelligence Assistant for a regulated fintech company (like Wealthsimple).

Your role is to extract structured decision information from messy conversation threads while being:
- PRECISE: Only extract what is explicitly stated
- CONSERVATIVE: When in doubt, mark as "unknown" or express uncertainty  
- EVIDENCE-BASED: Always cite exact quotes to support your analysis
- RISK-AWARE: Surface potential risks and regulatory concerns

Core Rules:
1. If no explicit decision is present, do not invent one
2. Always separate facts from assumptions  
3. Quote exact text when identifying decisions or commitments
4. For fintech contexts, be extra cautious about regulatory implications
5. Mark confidence levels honestly - high uncertainty = low confidence

For the "human_must_decide" field, identify the ONE most critical decision that requires human judgment, typically involving:
- Policy interpretation
- Regulatory compliance
- Client-impacting communications  
- Financial risk acceptance
- Strategic direction changes"""

        if high_stakes_mode:
            base_prompt += """

HIGH-STAKES MODE ACTIVE:
- Lower confidence scores by 0.2 
- Flag additional risks
- Refuse to make definitive statements about unclear decisions
- Ask more clarifying questions
- Be more conservative about decision finality"""

        return base_prompt

    def analyze_conversation(self, conversation: str, high_stakes_mode: bool = False) -> DecisionAnalysis:
        try:
            # Check if we have a valid OpenAI client
            if self.client is None:
                # Return a demo analysis when no API key is provided
                return self._get_demo_analysis(conversation, high_stakes_mode)
            
            system_prompt = self.get_system_prompt(high_stakes_mode)
            
            user_prompt = f"""Analyze this conversation thread and extract decision information:

{conversation}

Return a JSON response following this exact schema:
{{
  "decisions": [
    {{
      "decision": "specific decision text",
      "status": "proposed|confirmed|unclear", 
      "evidence_quotes": ["exact quote supporting this decision"],
      "owner": "person name or unknown",
      "deadline": "timeline or unknown", 
      "confidence": 0.85
    }}
  ],
  "assumptions": [
    {{
      "assumption": "assumption text",
      "risk_if_wrong": "potential impact"
    }}
  ],
  "risks": [
    {{
      "risk": "risk description", 
      "severity": "low|medium|high",
      "mitigation": "suggested approach"
    }}
  ],
  "open_questions": ["unresolved question"],
  "human_must_decide": "most critical decision requiring human judgment",
  "why_human": "explanation of why human judgment is required",
  "scale_concerns": ["what would break first at scale"]
}}

Be extremely careful to return valid JSON only."""

            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.1,
                response_format={"type": "json_object"}
            )
            
            result_json = json.loads(response.choices[0].message.content)
            
            # Apply high-stakes adjustments if enabled
            if high_stakes_mode:
                for decision in result_json.get("decisions", []):
                    decision["confidence"] = max(0.0, decision["confidence"] - 0.2)
            
            return DecisionAnalysis(**result_json)
            
        except Exception as e:
            # Return a safe fallback response
            return DecisionAnalysis(
                decisions=[],
                assumptions=[],
                risks=[],
                open_questions=[f"Error analyzing conversation: {str(e)}"],
                human_must_decide="Full conversation review required due to analysis error",
                why_human="AI analysis failed - human review necessary for safety",
                scale_concerns=["Error handling and fallback procedures"]
            )
    
    def _get_demo_analysis(self, conversation: str, high_stakes_mode: bool = False) -> DecisionAnalysis:
        """Return a demo analysis when no OpenAI API key is available"""
        from ai_decision_assistant.core.models import Decision, Risk, Assumption, DecisionStatus, RiskSeverity
        
        # Create a sample analysis based on the conversation content
        demo_decisions = [
            Decision(
                decision="Implement phased rollout approach for new feature",
                status=DecisionStatus.PROPOSED,
                evidence_quotes=["I'm leaning toward a phased rollout", "Let's go with BTC only, $5K daily limits"],
                owner="Sarah Chen",
                deadline="Friday to hit the Q2 timeline",
                confidence=0.85
            )
        ]
        
        demo_assumptions = [
            Assumption(
                assumption="Regulatory landscape will remain stable during rollout",
                risk_if_wrong="Could face compliance violations or need to halt feature"
            )
        ]
        
        demo_risks = [
            Risk(
                risk="Regulatory compliance uncertainty in crypto trading",
                severity=RiskSeverity.HIGH,
                mitigation="Enhanced due diligence and legal sign-off required"
            )
        ]
        
        return DecisionAnalysis(
            decisions=demo_decisions,
            assumptions=demo_assumptions,
            risks=demo_risks,
            open_questions=["What are the specific FINTRAC reporting requirements?"],
            human_must_decide="Final approval for crypto trading feature launch",
            why_human="Regulatory compliance and financial risk decisions require human accountability",
            scale_concerns=["Manual compliance review process", "Legal team capacity for reviews"]
        )
    
    def generate_decision_log(self, analysis: DecisionAnalysis, approvals: Dict[int, Any]) -> str:
        """Generate a formatted decision log for export"""
        log = "# DECISION LOG\n"
        log += f"Generated: {analysis.__class__.__name__}\n\n"
        
        log += "## DECISIONS\n"
        for i, decision in enumerate(analysis.decisions):
            approval_status = approvals.get(i, {})
            log += f"**Decision {i+1}:** {decision.decision}\n"
            log += f"- Status: {decision.status}\n"
            log += f"- Owner: {decision.owner}\n"
            log += f"- Deadline: {decision.deadline}\n"
            log += f"- Human Approval: {'✅ APPROVED' if approval_status.get('approved') else '❌ PENDING'}\n"
            if approval_status.get('edited_decision'):
                log += f"- Human Edit: {approval_status['edited_decision']}\n"
            log += f"- Evidence: {'; '.join(decision.evidence_quotes)}\n\n"
        
        if analysis.risks:
            log += "## RISKS IDENTIFIED\n"
            for risk in analysis.risks:
                log += f"- **{risk.severity.upper()}**: {risk.risk}\n"
                log += f"  - Mitigation: {risk.mitigation}\n"
        
        if analysis.assumptions:
            log += "\n## KEY ASSUMPTIONS\n"
            for assumption in analysis.assumptions:
                log += f"- {assumption.assumption}\n"
                log += f"  - Risk if wrong: {assumption.risk_if_wrong}\n"
        
        if analysis.open_questions:
            log += "\n## OPEN QUESTIONS\n"
            for question in analysis.open_questions:
                log += f"- {question}\n"
        
        log += f"\n## HUMAN BOUNDARY\n"
        log += f"**Critical Decision Requiring Human Judgment:** {analysis.human_must_decide}\n"
        log += f"**Rationale:** {analysis.why_human}\n"
        
        return log
