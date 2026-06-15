---
name: environment-consulting-report-writing-skill
description: Chinese environmental consulting report writing and review skill for environmental consulting, research and demonstration reports, environmental impact analysis, pollution control studies, ecological/environmental risk assessment, technical due diligence, feasibility demonstration, monitoring plans, implementation plans, expert review response notes, and government-facing technical briefing materials. Use when Codex needs to draft, revise, condense, structure, or review Chinese environmental consulting reports with strong evidence chains, regulatory basis, impact reasoning, scenario comparison, conclusion boundaries, and actionable mitigation measures.
---

# Environment Consulting Report Writing

## Core Positioning

Treat each output as a formal Chinese environmental consulting technical document. Prioritize evidence-based reasoning over generic positive language. Do not impose a fixed table of contents; adapt structure to the user's project, requested section, and approval or consulting context.

Default report logic:

> project need -> regulatory and technical basis -> evaluation boundary -> environmental baseline or problem -> method and scenario -> impact or risk analysis -> comparative judgement -> mitigation or management measures -> conditional conclusion -> follow-up work

## Workflows

### Draft or Rewrite Text

1. Identify the report type: research/demonstration report, environmental impact analysis, risk assessment, monitoring plan, implementation plan, expert response, or briefing material.
2. Clarify the analysis object, spatial/temporal boundary, evaluation indicators, data sources, and applicable standards from the user's material.
3. Organize paragraphs by "object -> basis/fact -> comparison/analysis -> judgement -> management implication".
4. Preserve necessary project facts, numbers, standards, and document names. Do not invent regulatory conclusions, monitoring data, approvals, or compliance status.
5. Output directly replaceable Chinese report text unless the user asks for comments or a problem list.

### Review Report Logic

Check whether the section has:

- Clear positioning: what problem the section answers and what object it analyzes.
- Evidence chain: monitoring, survey, model, experiment, design document, policy/standard, expert opinion, case comparison, or defensible technical inference.
- Consistent criteria: same indicators, units, statistical periods, spatial boundaries, and judgement basis for comparable objects.
- Bounded conclusions: no absolute promises such as "no impact", "ensure compliance", or "no risk".
- Actionable measures: object, measure, trigger condition, frequency or timing, responsible direction, and follow-up use.

### Condense Text

Remove repeated background, generic policy explanation, slogan-like conclusions, and excessive self-explanation. Keep facts, indicators, standards, data ranges, scenario names, impact objects, and management requirements.

### Expert Review Response

For expert comments, use this structure:

> comment focus -> revision basis -> revised content/location -> remaining boundary or follow-up requirement

Keep the tone respectful and technical. Do not write defensive explanations. Make the revision traceable.

## Resource Navigation

Read only the reference file needed for the task:

- [report-logic.md](references/report-logic.md): section logic, evidence chains, comparison criteria, and conclusion boundaries.
- [environment-consulting-patterns.md](references/environment-consulting-patterns.md): common environmental consulting report types and section patterns.
- [language-rules.md](references/language-rules.md): wording rules, cautious expressions, and replacements for vague claims.
- [review-checklist.md](references/review-checklist.md): final review checklist.
- [prompt-library.md](references/prompt-library.md): reusable Chinese prompts for drafting, revision, review, condensation, and expert responses.
- [avoid_phrases.csv](data/avoid_phrases.csv): high-frequency weak expressions and preferred replacements.
- [check_report_style.py](scripts/check_report_style.py): optional local scanner for Chinese report text or docx files.

## Output Rules

- Use formal, stable, engineering-consulting Chinese.
- Write the main conclusion after its basis, not before it.
- Prefer concrete objects and indicators over abstract words such as "systematic", "comprehensive", "scientific", "reasonable", and "controllable".
- For laws, standards, plans, EIA documents, feasibility studies, preliminary design, or special studies, include full name, year, document number or issue/approval time when available.
- When information is missing, state the missing item and draft with a cautious placeholder instead of fabricating.
- When revising a user-provided paragraph, keep the original technical meaning unless the user explicitly asks for stronger judgement.
