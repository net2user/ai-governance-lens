# AI Model Risk Readiness Assistant

A readiness screening tool that assesses AI and machine learning models against
India's RBI Draft Guidance on Regulatory Principles for Model Risk Management
(released June 2026) and the earlier FREE-AI framework.

## The Problem

India's financial regulator now requires every bank and NBFC to run AI models
under a board-approved risk framework, covering five pillars: board-approved
governance including third-party vendor models, risk-based tiering by
materiality, complexity, and autonomy, human-in-the-loop oversight for
high-stakes decisions, explainability for high-risk models like credit
scoring, and independent validation separate from the build team. On top of
that sits a mandatory kill switch requirement for every model.

Most compliance officers and risk managers evaluating an AI model, whether
built in-house or bought from a vendor, have no fast way to check where that
model stands against these specific requirements.

## What This Tool Does

Given a short description of a model, what it does, who built it, how
autonomous it is, and what kind of decision it touches, this tool runs a
structured readiness read against each of the five pillars plus the kill
switch requirement, returning a plain-language gap check rather than a
compliance certification.

This is a screening aid, not legal or regulatory advice. See the disclaimer
shown on every result.

## Project Status

This is an active build. The assessment flow currently runs on placeholder
reasoning logic (see `src/assessment_flow.py`); the next phase wires in a
real reasoning model call grounded in the framework reference in
`src/framework_reference.py`.

## Structure

- `src/framework_reference.py`: structured summary of the five pillars and
  kill switch requirement, the grounding text the assessment checks against.
- `src/assessment_flow.py`: the assessment logic, currently a skeleton.
- `app/streamlit_app.py`: the interface.
- `scenarios/sample_models.json`: synthetic example models spanning a range
  of risk levels, for testing without needing real institutional data.

## Running Locally

```
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Regulatory Status

RBI released the draft Guidance on Regulatory Principles for Model Risk
Management, 2026 on June 24, 2026 (Press Release 2026-2027/528). The public
comment window closed July 24, 2026. As of this writing, RBI has not yet
published the final circular; the implementation timeline will be specified
once final guidance is issued. This tool is grounded in the draft language
and will be updated once the final version is released, since RBI's review
of stakeholder feedback could sharpen or shift the pillar requirements
before they take effect.

## Disclaimer

This tool is grounded in RBI's draft guidance as of June 2026. Final
guidance may differ from the draft language this tool currently reflects.
Check RBI's official notifications for the current regulatory position.
