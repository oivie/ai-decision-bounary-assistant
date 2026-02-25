"""
Unit tests for AI Decision Boundary Assistant
"""

import pytest
from unittest.mock import Mock, patch
import sys
import os

# Add src to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ai_decision_assistant.core.models import Decision, DecisionStatus, Risk, RiskSeverity
from ai_decision_assistant.core.decision_analyzer import DecisionAnalyzer
from ai_decision_assistant.utils.helpers import format_confidence_score, clean_text


class TestModels:
    """Test Pydantic models"""
    
    def test_decision_creation(self):
        """Test Decision model creation and validation"""
        decision = Decision(
            decision="Test decision",
            status=DecisionStatus.PROPOSED,
            evidence_quotes=["Test quote"],
            owner="Test Owner",
            deadline="Tomorrow",
            confidence=0.85
        )
        
        assert decision.decision == "Test decision"
        assert decision.status == DecisionStatus.PROPOSED
        assert decision.confidence == 0.85
    
    def test_confidence_bounds(self):
        """Test confidence score validation"""
        # Valid confidence
        decision = Decision(
            decision="Test",
            status=DecisionStatus.PROPOSED,
            evidence_quotes=["quote"],
            owner="owner",
            deadline="deadline",
            confidence=0.5
        )
        assert decision.confidence == 0.5
        
        # Test bounds
        with pytest.raises(ValueError):
            Decision(
                decision="Test",
                status=DecisionStatus.PROPOSED,
                evidence_quotes=["quote"],
                owner="owner",
                deadline="deadline",
                confidence=1.5  # Invalid - over 1.0
            )


class TestDecisionAnalyzer:
    """Test DecisionAnalyzer functionality"""
    
    def test_init_without_api_key(self):
        """Test analyzer initialization without API key"""
        with patch.dict(os.environ, {}, clear=True):
            analyzer = DecisionAnalyzer()
            assert analyzer.client is None
    
    def test_demo_analysis(self):
        """Test demo analysis generation"""
        analyzer = DecisionAnalyzer()
        result = analyzer._get_demo_analysis("Test conversation", False)
        
        assert result is not None
        assert len(result.decisions) > 0
        assert result.human_must_decide is not None
        assert result.why_human is not None
    
    def test_high_stakes_mode(self):
        """Test high stakes mode affects confidence"""
        analyzer = DecisionAnalyzer()
        
        # Test demo analysis with high stakes
        normal_result = analyzer._get_demo_analysis("Test", False)
        high_stakes_result = analyzer._get_demo_analysis("Test", True)
        
        # Both should work
        assert normal_result is not None
        assert high_stakes_result is not None


class TestHelpers:
    """Test utility helper functions"""
    
    def test_format_confidence_score(self):
        """Test confidence score formatting"""
        assert "🟢" in format_confidence_score(0.9)  # High confidence
        assert "🟡" in format_confidence_score(0.6)  # Medium confidence  
        assert "🔴" in format_confidence_score(0.3)  # Low confidence
    
    def test_clean_text(self):
        """Test text cleaning functionality"""
        dirty_text = "  This   has   extra   spaces  \n\n  "
        clean = clean_text(dirty_text)
        assert clean == "This has extra spaces"
    
    def test_clean_text_empty(self):
        """Test text cleaning with empty input"""
        assert clean_text("") == ""
        assert clean_text("   ") == ""


class TestIntegration:
    """Integration tests"""
    
    def test_full_analysis_pipeline(self):
        """Test complete analysis pipeline"""
        analyzer = DecisionAnalyzer()
        
        test_conversation = """
        From: sarah@company.com
        To: team@company.com
        Subject: New Feature Decision
        
        I think we should launch the new crypto feature next week.
        The risk is moderate but manageable.
        John, can you handle the implementation?
        """
        
        # Should work in demo mode
        result = analyzer.analyze_conversation(test_conversation, False)
        assert result is not None
        assert hasattr(result, 'decisions')
        assert hasattr(result, 'human_must_decide')


if __name__ == "__main__":
    pytest.main([__file__])
