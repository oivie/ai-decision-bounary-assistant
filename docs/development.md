# Development Guide

## Project Structure

```
ai-decision-boundary-assistant/
├── src/ai_decision_assistant/     # Main package
│   ├── core/                      # Core business logic
│   │   ├── models.py              # Pydantic data models  
│   │   └── decision_analyzer.py   # AI analysis engine
│   ├── ui/                        # User interface
│   │   └── app.py                 # Streamlit application
│   ├── data/                      # Sample data and scenarios
│   │   └── sample_scenarios.py    # Demo conversation threads
│   └── utils/                     # Utility functions
│       ├── helpers.py             # Helper functions
│       └── exceptions.py          # Custom exceptions
├── config/                        # Configuration
│   └── settings.py                # App configuration
├── tests/                         # Test suite
│   └── test_decision_assistant.py # Unit tests
├── docs/                          # Documentation
├── examples/                      # Usage examples
└── requirements.txt               # Dependencies
```

## Development Setup

1. **Clone and Setup**
   ```bash
   git clone <repository>
   cd ai-decision-boundary-assistant
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e .[dev]  # Install with development dependencies
   ```

3. **Configuration**
   ```bash
   cp .env.template .env
   # Edit .env with your OpenAI API key (optional for demo mode)
   ```

4. **Run Tests**
   ```bash
   pytest tests/ -v
   pytest --cov=ai_decision_assistant tests/  # With coverage
   ```

5. **Run Application**
   ```bash
   python run_app.py
   # Or directly: streamlit run src/ai_decision_assistant/ui/app.py
   ```

## Code Style

- **Formatting**: Use `black` for code formatting
- **Linting**: Use `flake8` for linting
- **Type Hints**: Use type hints throughout
- **Docstrings**: Follow Google style docstrings

```bash
# Format code
black src/ tests/

# Lint code  
flake8 src/ tests/

# Type checking
mypy src/
```

## Testing Strategy

- **Unit Tests**: Test individual components in isolation
- **Integration Tests**: Test component interactions
- **Demo Mode Tests**: Ensure functionality without API keys
- **Error Handling**: Test edge cases and error conditions

## Adding New Features

1. **Models**: Add new Pydantic models in `core/models.py`
2. **Analysis Logic**: Extend `DecisionAnalyzer` in `core/decision_analyzer.py`
3. **UI Components**: Add Streamlit components in `ui/app.py`
4. **Utilities**: Add helper functions in `utils/helpers.py`
5. **Tests**: Add corresponding tests in `tests/`

## Release Process

1. Update version in `setup.py` and `src/ai_decision_assistant/__init__.py`
2. Update `CHANGELOG.md` with new features
3. Run full test suite: `pytest tests/`
4. Build package: `python setup.py sdist bdist_wheel`
5. Tag release: `git tag v0.1.0`

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Make changes with tests
4. Ensure all tests pass
5. Submit pull request

## Architecture Decisions

### Why Pydantic Models?
- Strong data validation and serialization
- Automatic API documentation generation  
- Type safety and IDE support

### Why Streamlit?
- Rapid prototyping for ML/AI applications
- Built-in components for data visualization
- Easy deployment and sharing

### Why Modular Structure?
- Separation of concerns (UI, business logic, data)
- Easier testing and maintenance
- Cleaner imports and dependencies
- Enables future refactoring (e.g., different UI frameworks)
