"""
Assessment flow skeleton.

This defines the shape of the LangGraph flow that scores a model description
against the five pillars plus the kill switch requirement. The reasoning
step (call_reasoning_model) is a placeholder until API keys are wired in.

Phase 1 work: replace the placeholder logic in call_reasoning_model with a
real call to the chosen provider (Anthropic or OpenAI), using
framework_reference.py as grounding context in the system prompt.
"""

from typing import TypedDict, List
from framework_reference import FIVE_PILLARS, KILL_SWITCH_REQUIREMENT, DISCLAIMER


class ModelInput(TypedDict):
    name: str
    description: str
    built_by: str          # "in_house" or "third_party_vendor"
    decision_type: str
    autonomy_level: str
    customer_impact: str


class PillarResult(TypedDict):
    pillar: str
    status: str             # "likely_covered" / "gap" / "unclear_needs_input"
    reasoning: str


class AssessmentResult(TypedDict):
    model_name: str
    pillar_results: List[PillarResult]
    kill_switch_result: PillarResult
    overall_summary: str
    disclaimer: str


def call_reasoning_model(model_input: ModelInput, pillar_key: str, pillar_def: dict) -> PillarResult:
    """
    Placeholder reasoning step.

    Phase 1: replace this with a real call to the stronger reasoning model
    (e.g. Claude or GPT), passing pillar_def['requirement'] and
    pillar_def['check_questions'] as grounding, plus model_input as the
    scenario being assessed. The model should return a status and a short
    plain-language reasoning string, not a certification.
    """
    return {
        "pillar": pillar_def["name"],
        "status": "unclear_needs_input",
        "reasoning": (
            "Placeholder result. Wire in a reasoning model call here using "
            f"the check questions for '{pillar_def['name']}' against the "
            "model description provided."
        ),
    }


def run_assessment(model_input: ModelInput) -> AssessmentResult:
    pillar_results = []
    for key, pillar_def in FIVE_PILLARS.items():
        result = call_reasoning_model(model_input, key, pillar_def)
        pillar_results.append(result)

    kill_switch_result = call_reasoning_model(
        model_input, "kill_switch", KILL_SWITCH_REQUIREMENT
    )

    return {
        "model_name": model_input["name"],
        "pillar_results": pillar_results,
        "kill_switch_result": kill_switch_result,
        "overall_summary": (
            "Placeholder summary. Phase 1 will generate a real plain-language "
            "readiness summary once the reasoning step is wired in."
        ),
        "disclaimer": DISCLAIMER,
    }


if __name__ == "__main__":
    import json
    with open("../scenarios/sample_models.json") as f:
        scenarios = json.load(f)

    sample = scenarios[0]
    test_input: ModelInput = {
        "name": sample["name"],
        "description": sample["description"],
        "built_by": sample["built_by"],
        "decision_type": sample["decision_type"],
        "autonomy_level": sample["autonomy_level"],
        "customer_impact": sample["customer_impact"],
    }
    result = run_assessment(test_input)
    print(json.dumps(result, indent=2))
