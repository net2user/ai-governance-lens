"""
Grounding reference for the assessment engine.

This module holds a structured summary of RBI's Draft Guidance on Regulatory
Principles for Model Risk Management, 2026 (released June 23-24, 2026) and the
earlier FREE-AI framework. It is the source of truth the reasoning step checks
model descriptions against. Update this file if final guidance changes the
pillar language after the July 24, 2026 comment window closes.
"""

FIVE_PILLARS = {
    "board_approved_mrm": {
        "name": "Board-Approved Model Risk Management Framework",
        "requirement": (
            "Every regulated entity must have a formal, board-approved policy "
            "covering the full lifecycle of every AI/ML model, including "
            "third-party models procured from vendors. Third-party models "
            "cannot be treated as an unaccountable black box."
        ),
        "check_questions": [
            "Is this model covered under a board-approved MRM policy?",
            "If this model is from a vendor, is it explicitly included in "
            "that policy rather than exempted as external?",
        ],
    },
    "risk_based_tiering": {
        "name": "Risk-Based Model Tiering",
        "requirement": (
            "Models must be classified by materiality (how much a wrong "
            "output costs), complexity (how hard it is to understand or "
            "validate), and autonomy (how much it acts without human "
            "intervention). High-risk models face stricter pre-deployment "
            "assessment."
        ),
        "check_questions": [
            "What is the materiality of this model's output?",
            "How complex or opaque is the model to validate?",
            "How autonomous is the model's decision-making?",
        ],
    },
    "human_in_the_loop": {
        "name": "Human-in-the-Loop Oversight",
        "requirement": (
            "High-risk automated decisions must have defined human review "
            "checkpoints. No decision significantly affecting a customer's "
            "financial life can be made entirely by an AI system without "
            "human oversight."
        ),
        "check_questions": [
            "Does a human review this model's high-stakes outputs before "
            "they take effect?",
            "Is there a documented escalation path when the model is "
            "uncertain?",
        ],
    },
    "explainability": {
        "name": "Explainability, No Black Boxes",
        "requirement": (
            "High-risk models, credit scoring in particular, must produce "
            "human-readable explanations for their outputs that regulators, "
            "auditors, and affected customers can scrutinize."
        ),
        "check_questions": [
            "Can this model explain, in plain language, why it reached a "
            "given output?",
            "Would that explanation satisfy an auditor or an affected "
            "customer, not just an engineer?",
        ],
    },
    "independent_validation": {
        "name": "Independent Validation",
        "requirement": (
            "Models cannot be validated only by the team that built and "
            "deployed them. An independent validation function must "
            "regularly test, stress-test, and challenge the model."
        ),
        "check_questions": [
            "Is there a validation function separate from the build team "
            "reviewing this model?",
            "Has the model been stress-tested outside its original design "
            "assumptions?",
        ],
    },
}

KILL_SWITCH_REQUIREMENT = {
    "name": "AI Kill Switch",
    "requirement": (
        "Every AI/ML model must have a clearly documented mechanism to "
        "instantly override, suspend, or completely deactivate it if it "
        "begins behaving outside expected parameters."
    ),
    "check_questions": [
        "Is there a documented, immediate deactivation pathway for this "
        "model?",
        "Has that pathway actually been tested, not just written down?",
    ],
}

DISCLAIMER = (
    "This is a readiness screening aid, not a compliance certification and "
    "not a substitute for legal or regulatory sign-off. Final RBI guidance "
    "may differ from the June 2026 draft this tool is grounded in."
)
