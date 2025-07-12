# /learn Command: Iterative Context Learning for ADO/TRN

This command processes CONTEXT.md and discussions to build/evolve understanding. The goal is to be able to create docs/PLANNING.md and docs/CONTEXT.md to the fullest extent possible. PLANNING.md must be a comprehensive plan from init to production deployment for beta testing. CONTEXT.md must be a comprehensive list of assumptions and preferences to validate against. 

$ARGUMENTS = The latest discussion reply

Steps:
1. Read /docs/CONTEXT.md (assumptions/preferences).
2. Scan /docs/discussions/ for DISCUSSION_*.md files.
3. If none: Generate DISCUSSION_001.md with basic questions on project (vision, tech, etc.).
4. If exist: Analyze chain; generate NEXT DISCUSSION_N.md with responses/follow-ups/questions. (Do Not Edit it)
5. Research gaps using tools (e.g., web_search for trends).
6. Edit CONTEXT.md: Append new assumptions/learnings (one-per-line).
7. Edit PLANNING.md in the root folder to align with new assumptions/learnings.
8. Output: Summary of updates; link to new DISCUSSION.md.