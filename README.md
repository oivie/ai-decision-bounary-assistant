# AI Decision Boundary Assistant

A sophisticated AI system that transforms messy conversation threads into structured decision documentation while maintaining clear human accountability boundaries. Built for regulated industries like fintech where decision transparency and audit trails are critical.

## 🎯 What It Does

Converts unstructured conversations (emails, Slack threads, meeting notes) into:
- **Structured Decisions** with confidence scores and evidence citations
- **Risk Analysis** with severity levels and mitigation strategies  
- **Human Accountability Gates** requiring explicit approval for critical decisions
- **Audit-Ready Documentation** for compliance and governance

## 🚀 Quick Start

### **Instant Demo** (No setup required)

```bash
git clone <repository>
cd ai-decision-boundary-assistant
python3 demo.py
```

Visit **http://localhost:8501** and try the sample scenarios!

### **Alternative Demo Methods**

```bash
# Method 1: Make command
make demo

# Method 2: Direct Streamlit  
PYTHONPATH=src python3 -m streamlit run src/ai_decision_assistant/ui/app.py

# Method 3: Bash script
./start_demo.sh
```

### **Command Line Demo**
```bash
PYTHONPATH=src python3 cli.py --text "We decided to launch next week. Sarah will handle compliance."
```

## 📁 Project Structure

```
ai-decision-boundary-assistant/
├── src/ai_decision_assistant/     # Main package
│   ├── core/                      # Business logic
│   │   ├── models.py              # Pydantic data models
│   │   └── decision_analyzer.py   # AI analysis engine
│   ├── ui/                        # Streamlit interface
│   │   └── app.py                 # Web application
│   ├── data/                      # Sample scenarios
│   │   └── sample_scenarios.py    # Demo conversations
│   └── utils/                     # Utilities
│       ├── helpers.py             # Helper functions
│       └── exceptions.py          # Custom exceptions
├── config/                        # Configuration
│   └── settings.py                # App settings
├── tests/                         # Test suite
├── docs/                          # Documentation
├── examples/                      # Usage examples
└── requirements.txt               # Dependencies
```

## 🛠 Development

### Setup Development Environment

```bash
pip install -e .[dev]  # Install with development dependencies
```

### Run Tests

```bash
pytest tests/ -v
pytest --cov=ai_decision_assistant tests/  # With coverage
```

### Code Quality

```bash
black src/ tests/        # Format code
flake8 src/ tests/       # Lint code  
mypy src/                # Type checking
```

## 🔧 Features

### Core Capabilities
- **AI-Native Decision Extraction**: Automatically identifies decisions, risks, and ownership
- **Evidence-Based Analysis**: Cites exact quotes supporting each finding
- **Confidence Scoring**: Shows AI certainty levels with color coding
- **Human Boundary Gates**: Explicit approval required for critical decisions
- **High-Stakes Mode**: More conservative analysis for critical situations

### Safety & Governance  
- **Conservative AI Behavior**: Marks uncertain extractions as "unknown"
- **Human-in-the-Loop**: AI never makes final decisions, only structures information
- **Audit Trail**: Complete decision logs with approvals and timestamps
- **Regulatory Aware**: Built for fintech compliance requirements

## 📊 Usage Examples

### Basic Analysis
```python
from ai_decision_assistant.core.decision_analyzer import DecisionAnalyzer

analyzer = DecisionAnalyzer()
result = analyzer.analyze_conversation(conversation_text)

print(f"Found {len(result.decisions)} decisions")
print(f"Critical decision: {result.human_must_decide}")
```

### Streamlit Interface
- Load sample scenarios or paste your own conversations
- Review extracted decisions with confidence scores
- Approve decisions and add human accountability
- Export audit-ready decision logs

## 🔍 Key Design Principles

1. **Human-AI Collaboration**: AI handles cognitive load, humans make final decisions
2. **Transparency**: Every decision includes evidence quotes and confidence scores  
3. **Safety First**: Conservative behavior with multiple approval gates
4. **Regulatory Ready**: Built for compliance and audit requirements
5. **Scalable Design**: Handles enterprise workflow adoption

## 🎯 Perfect For

- **Fintech Teams**: Regulatory compliance and risk management
- **Product Managers**: Documenting feature decisions and trade-offs
- **Executive Teams**: Board meeting follow-ups and strategic decisions  
- **Compliance Teams**: Creating audit trails for regulatory reviews
- **Any Organization**: Where decision accountability matters

## 📚 Documentation

- [API Reference](docs/api.md) - Detailed API documentation
- [Development Guide](docs/development.md) - Contributing and architecture
- [Examples](examples/) - Usage examples and tutorials

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make changes with tests
4. Ensure tests pass: `pytest tests/`
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.
