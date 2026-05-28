# ADK 2.0 Agent Workshop

A starter scaffold for building agents with the
[Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/).

## Quick start

```bash
# Clone and enter
git clone https://github.com/Phoresight-io/adk-workshop.git
cd adk-workshop

# Virtual env
python3 -m venv .venv
source .venv/bin/activate

# Install
pip install google-adk>=2.0.0 python-dotenv

# Credentials
gcloud auth login
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID

# Enable required APIs
gcloud services enable \
  aiplatform.googleapis.com \
  cloudresourcemanager.googleapis.com \
  run.googleapis.com \
  cloudbuild.googleapis.com

# Copy and verify env
cp .env.example .env

# Run
adk run agents/root_agent
```

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

3. **Configure credentials** — choose one of the two options below.

### Option A — Vertex AI + Application Default Credentials (recommended)

ADK reads ADC automatically when `GOOGLE_GENAI_USE_VERTEXAI=true`. No API key file required.

```bash
# Install the gcloud CLI: https://cloud.google.com/sdk/docs/install

# Authenticate your user account
gcloud auth login

# Write application default credentials (what ADK / the SDK reads at runtime)
gcloud auth application-default login

# Set your default project
gcloud config set project YOUR_PROJECT_ID

# Verify
gcloud config list
```

Then copy and edit the env file:

```bash
cp .env.example .env
# Set GOOGLE_CLOUD_PROJECT and GOOGLE_CLOUD_LOCATION; leave GOOGLE_GENAI_USE_VERTEXAI=true
```

### Option B — Google AI Studio API key

```bash
cp .env.example .env
# Comment out the Vertex AI block and set GOOGLE_API_KEY instead
```

Obtain a key at <https://aistudio.google.com/app/apikey>.

## Running the agent

Launch the interactive CLI:

```bash
adk run agents/root_agent
```

Or open the web UI:

```bash
adk web
```

## Deploying to Vertex AI Agent Engine

Use `adk deploy agent_engine` to push any agent to a managed, scalable endpoint on Vertex AI.

```bash
PROJECT_ID=your_gcp_project_id
LOCATION_ID=us-central1

adk deploy agent_engine \
    --project=$PROJECT_ID \
    --region=$LOCATION_ID \
    --display_name="Grant Tracker Agent" \
    agents/tracker_agent
```

After deployment the command prints a **resource name** of the form:
```
projects/<PROJECT_ID>/locations/<LOCATION_ID>/reasoningEngines/<ENGINE_ID>
```
Save that ID — you'll need it to call the agent programmatically via the Vertex AI SDK.

> **Note:** Cloud Build and Cloud Run APIs must be enabled (see quick start above).
> Deployment typically takes 3–5 minutes.

## Adding tools

1. Define a new function in `agents/root_agent/tools.py`.
   - Use Python type hints and a docstring — ADK derives the tool schema from them automatically.
2. Import and add the function to the `tools` list in `agents/root_agent/agent.py`.

## Adding sub-agents

Create a new package under `agents/` (e.g. `agents/search_agent/`) following the same
`agent.py` / `tools.py` / `__init__.py` pattern, then reference it as a sub-agent or
tool inside `root_agent`.
