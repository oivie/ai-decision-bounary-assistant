"""Custom exceptions for the AI Decision Boundary Assistant"""

class AIDecisionAssistantError(Exception):
    """Base exception for AI Decision Assistant"""
    pass

class AnalysisError(AIDecisionAssistantError):
    """Exception raised when conversation analysis fails"""
    pass

class ValidationError(AIDecisionAssistantError):
    """Exception raised when data validation fails"""
    pass

class ConfigurationError(AIDecisionAssistantError):
    """Exception raised when configuration is invalid"""
    pass

class APIError(AIDecisionAssistantError):
    """Exception raised when external API calls fail"""
    pass
