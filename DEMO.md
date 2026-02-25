# 🚀 Demo Instructions - AI Decision Boundary Assistant

## ✅ **Quick Start (Easiest)**

### **Option 1: Web Interface** (Recommended)
```bash
cd ai-decision-boundary-assistant
make demo
```
Then visit: **http://localhost:8501**

### **Option 2: Simple Script**
```bash
./start_demo.sh
```

### **Option 3: Direct Streamlit**
```bash
PYTHONPATH=src python3 -m streamlit run src/ai_decision_assistant/ui/app.py
```

## 🖥️ **Web Interface Demo Flow**

### **Step 1: Choose Sample Scenario**
In the sidebar, select from:
- **Risk/Compliance Decision** - Crypto trading feature approval
- **Product Launch** - Feature rollout discussion  
- **Customer Incident** - Security breach response

### **Step 2: Analyze Conversation**
1. Click **"🔍 Analyze Conversation"**
2. Watch AI extract structured decisions in seconds
3. Review confidence scores and evidence quotes

### **Step 3: Explore the 5 Tabs**

#### 🎯 **Tab 1: Decisions**
- See extracted decisions with owners and deadlines
- Check confidence scores (🟢 High, 🟡 Medium, 🔴 Low)
- Approve decisions with checkboxes
- Edit decisions if needed

#### ⚠️ **Tab 2: Risks & Assumptions** 
- Review key assumptions and their risks
- See color-coded risk levels
- Review mitigation strategies

#### 🚨 **Tab 3: Human Boundary**
- **Critical Decision**: What requires human judgment
- **AI Won't Decide**: Regulatory, financial, strategic decisions
- **Final Accountability**: Your responsibility confirmation

#### 📊 **Tab 4: Scale Concerns**
- What breaks first when scaling
- Operational bottlenecks
- Resource constraints

#### 📄 **Tab 5: Decision Log**
- Export audit-ready documentation
- Requires all approvals first
- Download markdown decision log

### **Step 4: Try Different Modes**
- Toggle **"High-Stakes Mode"** for conservative analysis
- Paste your own conversation in the text area
- Compare results across different scenarios

## 💻 **Command Line Demo**

### **Basic Text Analysis**
```bash
PYTHONPATH=src python3 cli.py --text "I think we should launch the crypto feature next week. Mike can you handle compliance?"
```

### **File Analysis**
```bash
echo "Meeting notes: We decided to proceed with the launch..." > test.txt
PYTHONPATH=src python3 cli.py --file test.txt --output decision_log.md
```

### **High-Stakes Analysis**
```bash
PYTHONPATH=src python3 cli.py --text "Board decision needed on regulatory response" --high-stakes
```

## 🎯 **Key Demo Points to Highlight**

### **1. Human-AI Collaboration**
- AI structures information, humans make decisions
- Multiple approval gates prevent AI overreach
- Explicit human accountability requirements

### **2. Transparency**
- Confidence scores show AI uncertainty
- Evidence quotes prove where decisions came from
- Clear separation between analysis and judgment

### **3. Enterprise Ready**
- Works without API keys (demo mode)
- Audit-ready documentation export
- Conservative approach for regulated industries

### **4. Real-World Scenarios**
- Fintech compliance decisions
- Product launch coordination
- Incident response management

## 🔧 **Demo Troubleshooting**

### **Import Errors**
```bash
# Always use PYTHONPATH=src
export PYTHONPATH=src
python3 -m streamlit run src/ai_decision_assistant/ui/app.py
```

### **Streamlit Not Found**
```bash
# Install Streamlit if missing
pip3 install streamlit
```

### **Port Already in Use**
```bash
# Use different port
python3 -m streamlit run src/ai_decision_assistant/ui/app.py --server.port=8502
```

## 📱 **Demo Script (5 minutes)**

1. **"Let me show you an AI system that helps teams make better decisions..."**
   
2. **Load Sample Scenario** (30 seconds)
   - Select "Risk/Compliance Decision" from dropdown
   - Show messy email thread about crypto feature

3. **AI Analysis** (1 minute)  
   - Click "Analyze Conversation"
   - Point out instant structured extraction
   - Highlight confidence scores and evidence quotes

4. **Human Boundaries** (2 minutes)
   - Tab through all 5 sections
   - Emphasize human approval requirements
   - Show "Human Boundary" tab - what AI won't decide

5. **Decision Export** (1 minute)
   - Approve a few decisions
   - Export decision log
   - Show audit-ready documentation

6. **Different Mode** (30 seconds)
   - Try high-stakes mode
   - Show how AI becomes more conservative

**Key Message**: *"AI handles the cognitive load of structuring information, but humans retain control of actual decisions. Perfect for regulated industries where accountability matters."*

## 🎉 **Expected Demo Outcomes**

Viewers will see:
- ✅ **Practical AI Application** solving real business problems
- ✅ **Human-Centered Design** with proper safety boundaries  
- ✅ **Enterprise Grade** functionality and documentation
- ✅ **Regulatory Awareness** built for compliance environments
- ✅ **Professional Engineering** with proper project structure

Perfect for demonstrating sophisticated AI system design that meaningfully expands human capabilities while maintaining appropriate boundaries! 🚀
