# Documentation Guidelines for ADO & TRN Alignment

To maintain alignment during build, all phases require specific docs. These ensure transparency, auditability, and eternal knowledge transfer. Generated per milestone via PRPs; stored in /docs or GitHub wiki. Format: MD with sections for overview, specs, risks, metrics, and user/developer guides.

## Required Per Phase/Milestone
- **Overview Doc**: High-level summary (goals, deliverables, ties to vision).
- **Technical Specs**: Detailed (e.g., contract APIs, AI params, UI wireframes).
- **User Guide**: For beta (e.g., dial usage, shard recovery).
- **Developer Guide**: For beta (e.g., dial usage, shard recovery).
- **Risk Update**: Ties to master plan; mitigations progress.
- **Validation Report**: Test results (gas, audits, simulations); pass/fail criteria.
- **Change Log**: Updates from prior (e.g., quorum tweaks).

## Ongoing/Global Docs
- **CLAUDE.md**: Rules are immutable.
- **CONTEXT.md**: Assumptions list; add as evolutions occur.
- **API/MCP Reference**: Auto-generated from code.
- **Audit/Bounty Reports**: Post-security events.
- **DAO Proposals**: On-chain logs + summaries.
- **Metrics Dashboard**: Real-time (DAU, peg stability); quarterly reviews.

## Generation Process
- Use PRP to create/update docs per INITIAL.md.
- Version control: Git commits with tags (e.g., v1.0-phase1).
- Accessibility: Public except sensitive (e.g., quantum keys).

This keeps us aligned—review via DAO.