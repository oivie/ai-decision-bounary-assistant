import streamlit as st
import json
import sys
import os

# Add src to Python path - navigate from ui/ up to project root, then to src/
current_file = os.path.abspath(__file__)
ui_dir = os.path.dirname(current_file)  # .../ui/
ai_decision_assistant_dir = os.path.dirname(ui_dir)  # .../ai_decision_assistant/
src_dir = os.path.dirname(ai_decision_assistant_dir)  # .../src/
project_root = os.path.dirname(src_dir)  # project root
actual_src_path = os.path.join(project_root, 'src')

if actual_src_path not in sys.path:
    sys.path.insert(0, actual_src_path)

from ai_decision_assistant.core.decision_analyzer import DecisionAnalyzer
from ai_decision_assistant.core.models import DecisionAnalysis, HumanApproval
from ai_decision_assistant.data.sample_scenarios import *

# Page configuration
st.set_page_config(
    page_title="AI Decision Boundary Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'analysis' not in st.session_state:
    st.session_state.analysis = None
if 'approvals' not in st.session_state:
    st.session_state.approvals = {}
if 'analyzer' not in st.session_state:
    st.session_state.analyzer = DecisionAnalyzer()

def main():
    st.title("⚖️ AI Decision Boundary Assistant")
    st.subheader("Transform messy conversations into structured decision documentation")
    
    # Sidebar for sample scenarios and settings
    with st.sidebar:
        st.header("🎯 Sample Scenarios")
        
        scenario_options = {
            "Custom Input": "",
            "Risk/Compliance Decision": """From: Sarah Chen <s.chen@wealthsimple.com>
To: Risk Committee <risk@wealthsimple.com>
Subject: New crypto trading feature - compliance review

Hey team,

We're looking to launch crypto trading for our premium users by Q2. Marketing is pushing hard for this given competitor pressure.

Key considerations:
- Regulatory landscape is still evolving in Canada
- We'd need additional KYC procedures for crypto trades
- Potential AML implications with large crypto positions
- Our current infrastructure can handle it technically

I'm leaning toward a phased rollout - start with BTC/ETH only, $10K daily limits, enhanced monitoring.

Thoughts? We need to decide by Friday to hit the Q2 timeline.

Sarah

---

From: Mike Rodriguez <m.rodriguez@wealthsimple.com>
Reply: I'm concerned about the regulatory risk. FINTRAC guidance on crypto reporting is still unclear. Can we get legal sign-off first?

---

From: Legal Team <legal@wealthsimple.com>
Reply: We can proceed with enhanced due diligence but recommend starting even smaller - $5K limits and BTC only initially.

---

From: Sarah Chen
Reply: Agreed. Let's go with BTC only, $5K daily limits, and full rollout pending regulatory clarity. I'll own the implementation timeline.""",
            
            "Product Launch Decision": """Alex Kim: Folks, we have a problem. The new portfolio rebalancing feature has a bug that affects users with >$500K portfolios. It's calculating tax efficiency incorrectly.

Jamie Walsh: How bad is the impact?

Alex Kim: About 3% of users could see suboptimal tax outcomes. Not huge dollar amounts but not great either.

Jamie Walsh: Options?
1. Delay launch by 2 weeks to fix
2. Launch with known issue, fix in patch  
3. Launch but exclude high-net-worth users temporarily

Sarah Liu: Marketing has already announced the March 15 launch date. Delay would be embarrassing.

Alex Kim: I vote for option 3. We can enable the feature for <$500K users immediately, fix the bug, then roll out to everyone.

Jamie Walsh: Risk is that HNW users might feel excluded. But I agree - better than broken functionality.

Alex Kim: I'll handle the communication to affected users. Timeline: launch March 15 for most users, full rollout by March 30.

Sarah Liu: Approved. I'll update marketing materials to reflect phased rollout.""",
            
            "Customer Incident": """From: Customer Success <cs@wealthsimple.com>
To: Product Team <product@wealthsimple.com>
Subject: URGENT - Trading halt affecting 50+ users

Team,

We have a critical issue. Our trading system is rejecting orders for about 50 users who have perfectly valid accounts. They're seeing "insufficient funds" errors even with adequate cash balances.

Customer impact:
- Users missing market opportunities
- Multiple complaints on social media  
- Some threatening to leave platform

Technical team says it's a caching issue that could take 6-8 hours to fully resolve.

Options:
1. Wait for full technical fix (6-8 hours)
2. Manual override for affected users (30 min per user)
3. Offer trading fee credits as compensation

I recommend option 2 + 3. We manually enable trading for these users immediately AND offer compensation.

This needs executive approval given the manual override process.

Mike Chen - Customer Success Lead

---

From: Head of Product
Reply: Approved for manual override. I'll personally authorize each one. Also approved for trading fee credits for affected users.

---

From: Mike Chen  
Reply: Perfect. I'll coordinate with ops team. Should have everyone back online within 2 hours."""
        }
        
        selected_scenario = st.selectbox("Choose a scenario:", list(scenario_options.keys()))
        
        st.header("⚙️ Settings")
        high_stakes_mode = st.checkbox(
            "High-Stakes Mode", 
            help="More conservative analysis with lower confidence scores"
        )
        
        if high_stakes_mode:
            st.warning("🔒 High-stakes mode enabled - AI will be more conservative")

    # Main input area
    st.header("📝 Input Conversation")
    
    default_text = scenario_options[selected_scenario] if selected_scenario != "Custom Input" else ""
    conversation = st.text_area(
        "Paste your conversation thread here:",
        value=default_text,
        height=300,
        help="Paste email threads, Slack conversations, or meeting notes"
    )

    # Analysis button
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("🔍 Analyze Conversation", type="primary"):
            if conversation.strip():
                with st.spinner("Analyzing conversation..."):
                    st.session_state.analysis = st.session_state.analyzer.analyze_conversation(
                        conversation, high_stakes_mode
                    )
                    st.session_state.approvals = {}  # Reset approvals
                st.success("Analysis complete!")
            else:
                st.error("Please enter a conversation to analyze")

    # Display results if analysis exists
    if st.session_state.analysis:
        display_analysis_results()

def display_analysis_results():
    analysis = st.session_state.analysis
    
    # Create tabs for different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🎯 Decisions", 
        "⚠️ Risks & Assumptions", 
        "🚨 Human Boundary",
        "📊 Scale Concerns", 
        "📄 Decision Log"
    ])
    
    with tab1:
        st.header("Extracted Decisions")
        
        if not analysis.decisions:
            st.info("No explicit decisions found in the conversation.")
        
        for i, decision in enumerate(analysis.decisions):
            with st.expander(f"Decision {i+1}: {decision.decision[:50]}...", expanded=True):
                # Decision details
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Status:** {decision.status}")
                    st.write(f"**Owner:** {decision.owner}")
                    st.write(f"**Deadline:** {decision.deadline}")
                with col2:
                    confidence_color = "green" if decision.confidence > 0.8 else "orange" if decision.confidence > 0.5 else "red"
                    st.write(f"**Confidence:** :{confidence_color}[{decision.confidence:.2f}]")
                
                st.write("**Evidence Quotes:**")
                for quote in decision.evidence_quotes:
                    st.write(f"> {quote}")
                
                # Human approval section
                st.subheader("Human Approval Required")
                
                approval_col1, approval_col2 = st.columns(2)
                with approval_col1:
                    approve = st.checkbox(f"Approve Decision {i+1}", key=f"approve_{i}")
                    edit_decision = st.text_input(
                        "Edit decision (if needed):", 
                        value=decision.decision,
                        key=f"edit_{i}"
                    )
                
                with approval_col2:
                    human_confirmation = st.text_area(
                        "Human confirmation statement:",
                        placeholder="I confirm this decision and accept accountability...",
                        key=f"confirm_{i}",
                        height=100
                    )
                
                # Store approval state
                st.session_state.approvals[i] = {
                    'approved': approve,
                    'edited_decision': edit_decision if edit_decision != decision.decision else "",
                    'human_confirmation': human_confirmation
                }
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🎯 Key Assumptions")
            if analysis.assumptions:
                for assumption in analysis.assumptions:
                    with st.expander(assumption.assumption[:50] + "..."):
                        st.write(f"**Assumption:** {assumption.assumption}")
                        st.write(f"**Risk if wrong:** {assumption.risk_if_wrong}")
            else:
                st.info("No key assumptions identified")
        
        with col2:
            st.subheader("⚠️ Risks Identified")
            if analysis.risks:
                for risk in analysis.risks:
                    severity_color = {"high": "red", "medium": "orange", "low": "blue"}[risk.severity]
                    with st.expander(f":{severity_color}[{risk.severity.upper()}] {risk.risk[:40]}..."):
                        st.write(f"**Risk:** {risk.risk}")
                        st.write(f"**Severity:** :{severity_color}[{risk.severity}]")
                        st.write(f"**Mitigation:** {risk.mitigation}")
            else:
                st.info("No specific risks identified")
        
        if analysis.open_questions:
            st.subheader("❓ Open Questions")
            for question in analysis.open_questions:
                st.write(f"- {question}")

    with tab3:
        st.header("🚨 Human Boundary Decision")
        
        st.error("**HUMAN CONFIRMATION REQUIRED**")
        
        st.write(f"**Critical Decision:** {analysis.human_must_decide}")
        st.write(f"**Why Human Required:** {analysis.why_human}")
        
        st.subheader("Accountability Gate")
        final_confirmation = st.checkbox(
            "I confirm the final decisions and accept full accountability", 
            key="final_confirmation"
        )
        
        if final_confirmation:
            st.success("✅ Human accountability confirmed")
        else:
            st.warning("⚠️ Human confirmation pending")
        
        st.info("""
        **AI Boundaries**: This system will NOT make decisions about:
        - Regulatory compliance interpretation
        - Client-facing communications approval  
        - Financial risk acceptance thresholds
        - Strategic policy changes
        """)

    with tab4:
        st.header("📊 What Breaks First at Scale")
        
        if analysis.scale_concerns:
            for concern in analysis.scale_concerns:
                st.write(f"- {concern}")
        
        st.subheader("Operational Considerations")
        st.write("""
        **Monitoring Requirements:**
        - Track AI confidence drift over time
        - Monitor false positive/negative rates
        - Human override frequency analysis
        
        **Failure Modes:**
        - Context window limitations with long conversations
        - Hallucination risks with ambiguous decisions
        - Consistency issues across different conversation styles
        
        **Scale Bottlenecks:**
        - Human approval queue management
        - Decision log storage and searchability
        - Integration with existing workflow tools
        """)

    with tab5:
        st.header("📄 Export Decision Log")
        
        # Check if all decisions are approved
        all_approved = all(
            st.session_state.approvals.get(i, {}).get('approved', False) 
            for i in range(len(analysis.decisions))
        )
        
        human_confirmed = st.session_state.get('final_confirmation', False)
        
        if all_approved and human_confirmed:
            st.success("✅ All decisions approved and human accountability confirmed")
            
            decision_log = st.session_state.analyzer.generate_decision_log(
                analysis, st.session_state.approvals
            )
            
            st.subheader("Generated Decision Log")
            st.text_area("Decision Log", value=decision_log, height=400)
            
            st.download_button(
                label="📥 Download Decision Log",
                data=decision_log,
                file_name="decision_log.md",
                mime="text/markdown"
            )
        else:
            st.warning("⚠️ Complete all approvals and human confirmation to generate decision log")
            missing = []
            if not all_approved:
                missing.append("Decision approvals")
            if not human_confirmed:
                missing.append("Human accountability confirmation")
            st.write(f"**Missing:** {', '.join(missing)}")

if __name__ == "__main__":
    main()
