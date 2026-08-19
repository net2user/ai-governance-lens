"""
Streamlit interface for the AI Model Risk Readiness Assistant.

Phase 2 skeleton. Run with: streamlit run app/streamlit_app.py
"""

import sys
import os
import json

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

import streamlit as st
from assessment_flow import run_assessment, ModelInput
from framework_reference import DISCLAIMER

st.set_page_config(page_title="AI Model Risk Readiness Assistant", page_icon="🛡️")

st.title("AI Model Risk Readiness Assistant")
st.caption(
    "Grounded in RBI's FREE-AI framework and the June 2026 draft Model Risk "
    "Management guidance."
)

with st.form("model_form"):
    name = st.text_input("Model name")
    description = st.text_area(
        "Describe what the model does, who built it, and how it's used"
    )
    built_by = st.selectbox("Built by", ["in_house", "third_party_vendor"])
    decision_type = st.text_input(
        "Decision type (e.g. credit_decisioning, fraud_detection)"
    )
    autonomy_level = st.selectbox(
        "Autonomy level",
        ["human_reviewed", "recommends_to_human", "fully_automated"],
    )
    customer_impact = st.selectbox(
        "Customer impact", ["none", "low", "medium", "high"]
    )
    submitted = st.form_submit_button("Run readiness check")

if submitted:
    model_input: ModelInput = {
        "name": name,
        "description": description,
        "built_by": built_by,
        "decision_type": decision_type,
        "autonomy_level": autonomy_level,
        "customer_impact": customer_impact,
    }
    result = run_assessment(model_input)

    st.subheader(f"Readiness read: {result['model_name']}")
    for pillar_result in result["pillar_results"]:
        st.markdown(f"**{pillar_result['pillar']}**: {pillar_result['status']}")
        st.write(pillar_result["reasoning"])

    st.markdown(f"**{result['kill_switch_result']['pillar']}**: "
                f"{result['kill_switch_result']['status']}")
    st.write(result["kill_switch_result"]["reasoning"])

    st.info(result["overall_summary"])
    st.caption(DISCLAIMER)

st.divider()
st.caption(DISCLAIMER)
