# ADK 2.0 Agent Workshop

A starter scaffold for building agents with the
[Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/).

## Project structure

```
agents/
└── root_agent/
    ├── __init__.py   # exports root_agent
    ├── agent.py      # Agent definition and configuration
    └── tools.py      # Tool functions (add your own here)
requirements.txt
.env.example
```

## Setup

1. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure credentials**

   ```bash
   cp .env.example .env
   # Open .env and set GOOGLE_API_KEY (or Vertex AI vars)
   ```

## Running the agent

Launch the interactive CLI:

```bash
adk run agents/root_agent
```

Or open the web UI:

```bash
adk web
```

## Adding tools

1. Define a new function in `agents/root_agent/tools.py`.
   - Use Python type hints and a docstring — ADK derives the tool schema from them automatically.
2. Import and add the function to the `tools` list in `agents/root_agent/agent.py`.

## Adding sub-agents

Create a new package under `agents/` (e.g. `agents/search_agent/`) following the same
`agent.py` / `tools.py` / `__init__.py` pattern, then reference it as a sub-agent or
tool inside `root_agent`.
