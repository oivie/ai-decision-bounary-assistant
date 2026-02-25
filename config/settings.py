# Configuration settings for AI Decision Boundary Assistant

import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration"""
    
    # API Configuration
    OPENAI_API_KEY: Optional[str] = os.getenv('OPENAI_API_KEY')
    OPENAI_MODEL: str = os.getenv('OPENAI_MODEL', 'gpt-4')
    
    # Application Settings
    APP_NAME: str = "AI Decision Boundary Assistant"
    APP_VERSION: str = "0.1.0"
    
    # Analysis Settings
    DEFAULT_TEMPERATURE: float = 0.1
    MAX_TOKENS: int = 4000
    CONFIDENCE_THRESHOLD_LOW: float = 0.5
    CONFIDENCE_THRESHOLD_HIGH: float = 0.8
    
    # High Stakes Mode Adjustments
    HIGH_STAKES_CONFIDENCE_PENALTY: float = 0.2
    
    # UI Configuration
    STREAMLIT_PAGE_TITLE: str = "AI Decision Boundary Assistant"
    STREAMLIT_PAGE_ICON: str = "⚖️"
    
    @classmethod
    def has_valid_api_key(cls) -> bool:
        """Check if a valid OpenAI API key is configured"""
        return bool(cls.OPENAI_API_KEY and cls.OPENAI_API_KEY != 'your-openai-key-here')
    
    @classmethod
    def get_confidence_color(cls, confidence: float) -> str:
        """Get color for confidence level"""
        if confidence >= cls.CONFIDENCE_THRESHOLD_HIGH:
            return "green"
        elif confidence >= cls.CONFIDENCE_THRESHOLD_LOW:
            return "orange"
        else:
            return "red"
