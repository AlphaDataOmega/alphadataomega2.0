# Ultimate Agentic StarterKit: Automated Project Builder

## Global Rules (CLAUDE.md Equivalent)
- Follow human dev flows: Plan (decompose specs), Implement (small chunks), Test/Iterate (loops), Review/Merge (advise/chain), Track/Alert (milestones/human input).
- Use OSS only: No paid APIs/services. Local-run via Docker.
- Agents: Role-based (Parser, Coder, Tester, Advisor) with self-correction (3 retries max before alert).
- LLMs: Ollama with Llama3/Mistral—prompt explicitly, reference examples to reduce hallucinations.
- Validation: Always run tests (unit/integration via code_execution); confidence >80% or re-plan.
- Alerts: On blockers/milestones, simulate email/GitHub issue (print or subprocess).
- Output: Modular code; commit to git if possible.
- Examples: Use patterns from below; extend for ADO-like projects (e.g., parse MD docs into milestones).

## Setup Instructions
1. Clone base StarterKit: git clone https://github.com/AlphaDataOmega/StarterKit
2. Add dependencies: pip install crewai autogen langgraph llama-index ollama gitpython requests pymupdf
3. Docker Compose for env: Include Ollama, n8n, OpenProject.
4. Run: python kit.py --overview your-project.md

## Examples Folder Patterns
- examples/parser.py: Extract milestones from MD (use LlamaIndex query: "List tasks as JSON").
- examples/coder.py: Gen code chunk (e.g., "From PRP: Build Solidity contract—output file.sol").
- examples/tester.py: Run tests (subprocess.call(['pytest'])); if fail, return error for iteration.
- examples/advisor.py: Review code (prompt: "Advise on improvements; chain with prior output").
- examples/workflow.json: n8n flow chaining agents.

## Feature Request: Build the Kit (Work-Order Style)
### FEATURE
Create/evolve the StarterKit into an agentic factory. Input: Project overview MD/PDF. Output: Built code with milestone reports. Flow:
1. Parse: Extract milestones/PRPs (JSON).
2. Decompose: Break into small tasks.
3. Agents Exec: Assign/implement/test/advise.
4. Merge/Track: Chain outputs; alert on complete/blocker.
Implement in Python; Dockerized.

### EXAMPLES
Reference above patterns. For ADO: Parse "32-week timeline" into {"milestone1": "CHAIN deploy"}.

### DOCUMENTATION
- CrewAI docs: https://docs.crew.ai (agents/roles).
- n8n: Self-host workflows (nodes for HTTP/JS).
- Ollama: ollama.run('llama3', prompt).
- LlamaIndex: For doc querying.

### OTHER CONSIDERATIONS
- Edge: Handle large docs (chunk parsing).
- Iteration: 3x loop per task.
- Human Alert: Print "ALERT: Review [issue]" or subprocess to GitHub API (use env token).
- Test: Include sample run with mini-overview MD.

