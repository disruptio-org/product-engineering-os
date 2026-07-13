---
name: grill-me
description: Run a relentless one-question-at-a-time interview to resolve every load-bearing branch in an idea, BRD, plan, or story.
disable-model-invocation: true
argument-hint: [document path or topic]
---

# Grill Me

Locate the target from `$ARGUMENTS`, the conversation, and `docs/product/`. Apply the `grilling` discipline.

Ask exactly one decision-bearing question per turn. Lead with a recommended default when evidence supports one. Explain consequences, challenge contradictions, and separate operational facts from design preferences.

Read the repository when evidence can answer the question. Update the source document as decisions settle. Record durable technical decisions under `docs/adr/`.

At completion, write `docs/product/<feature>/grill-summary.md` with decisions, facts, assumptions, rejected alternatives, remaining non-blocking questions, and the next recommendation.

Never invent an organizational fact.
