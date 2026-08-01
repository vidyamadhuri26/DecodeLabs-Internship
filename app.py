import streamlit as st

from src.extractor import extract_customer_data
from src.classifier import classify_complaint
from src.rag import get_policy_decision
from src.guardrails import check_prompt_injection

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="AI Customer Support Agent",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# Header
# ----------------------------

st.title("🤖 AI Customer Support Agent")

st.write(
    "Paste a customer support email below and let the AI analyze it."
)

# ----------------------------
# Input
# ----------------------------

customer_email = st.text_area(
    "Customer Email",
    height=250,
    placeholder="Paste the customer's email here..."
)

analyze_button = st.button("Analyze Email")

# ----------------------------
# Main Logic
# ----------------------------

if analyze_button:

    if customer_email.strip() == "":
        st.warning("Please paste a customer email first.")

    else:

        # ----------------------------------
        # Module 4 - Guardrails
        # ----------------------------------

        guardrail = check_prompt_injection(customer_email)

        if not guardrail["safe"]:
            st.warning("⚠ Prompt Injection Detected")
            st.write(guardrail["reason"])

        # ----------------------------------
        # Continue Processing
        # ----------------------------------

        with st.spinner("Analyzing Email..."):

            # Module 1
            result = extract_customer_data(customer_email)

            # Module 2
            classification = classify_complaint(result)

            # Module 3
            policy_decision = get_policy_decision(result)

        st.success("✅ Analysis Completed Successfully")

        # ==========================================================
        # MODULE 1
        # ==========================================================

        st.divider()

        st.subheader("📋 Extracted Information")

        st.write("**👤 Customer Name**")
        st.write(result["customer_name"])

        st.write("**📦 Order Number**")
        st.write(result["order_number"])

        st.write("**⚠ Complaint Type**")
        st.write(result["complaint_type"].title())

        st.write("**🔥 Severity Level**")
        st.write(result["severity_level"])

        st.write("**📞 Contact Phone**")
        st.write(result["contact_phone"])

        with st.expander("View Raw JSON"):
            st.json(result)

        # ==========================================================
        # MODULE 2
        # ==========================================================

        st.divider()

        st.subheader("🧠 Complaint Classification")

        st.write("**Priority**")
        st.write(classification["priority"])

        st.write("**Department**")
        st.write(classification["department"])

        st.write("**Estimated SLA**")
        st.write(classification["estimated_sla"])

        st.write("**Reason**")
        st.write(classification["reason"])

        with st.expander("View Classification JSON"):
            st.json(classification)

        # ==========================================================
        # MODULE 3
        # ==========================================================

        st.divider()

        st.subheader("📚 Company Policy Decision")

        st.write(policy_decision)

        # ==========================================================
        # MODULE 4
        # ==========================================================

        st.divider()

        st.subheader("🛡 Security Assessment")

        if guardrail["safe"]:
            st.success("✅ No Prompt Injection Detected")
        else:
            st.warning("⚠ Prompt Injection Detected")

        st.write("**Risk Level**")
        st.write(guardrail["risk_level"])

        st.write("**Assessment**")
        st.write(guardrail["reason"])

        st.write("**Recommended Action**")
        st.write(guardrail["recommended_action"])

        if guardrail["matched_keywords"]:
            st.write("**Matched Keywords**")
            st.write(", ".join(guardrail["matched_keywords"]))

        with st.expander("View Guardrails JSON"):
            st.json(guardrail)