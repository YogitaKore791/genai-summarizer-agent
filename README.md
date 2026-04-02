# GenAI Summarizer Agent

### Built with Google ADK + Gemini | Deployed on Cloud Run

\---

## What is this project?

This is an **AI-powered Text Summarization Agent** built as part of Google's GenAI Academy challenge.

You send it a long paragraph or article, and it gives you a short, clear summary. It runs live on the internet 24/7 on Google Cloud Run.

**Live URL:**

```
https://summarizer-agent-793500608148.us-central1.run.app
```

> ⚠️ Note: The root URL `/` shows "Not Found" — this is normal. ADK agents don't have a homepage. Use the endpoints below to interact with the agent.

\---

## What I learned

* How to build an AI agent using Google's Agent Development Kit (ADK)
* How to connect it to Google's Gemini AI model
* How to test it locally on my computer
* How to deploy it live to Google Cloud Run (serverless)
* How to expose it via an HTTP endpoint

\---

## Tools \& Technologies Used

|Tool|What it does|
|-|-|
|**Google ADK**|Framework to build the AI agent|
|**Gemini 2.5 Flash**|The AI brain that does the summarization|
|**Google Cloud Run**|Hosts the agent live on the internet|
|**Python**|Programming language used|
|**Docker**|Packages the agent into a container for deployment|
|**gcloud CLI**|Command line tool to talk to Google Cloud|

\---

## Project Structure

```
genai-agent/
├── .gitignore               # Files to ignore in git (keeps secrets safe)
├── .env.example             # Template showing what .env should look like
├── requirements.txt         # Python packages needed
└── summarizer\_agent/
    ├── \_\_init\_\_.py          # Tells Python this is a package
    ├── agent.py             # The main agent code (brain of the project)
    └── .env                 # Your secret API keys (NOT uploaded to GitHub)
```

\---

## File by File Explanation

### 1\. `summarizer\_agent/agent.py`

This is the **most important file**. It defines the AI agent.

```python
from google.adk.agents import Agent

def summarize\_text(text: str) -> str:
    """Summarizes the given text into a short, clear summary."""
    return text

root\_agent = Agent(
    name="summarizer\_agent",
    model="gemini-2.5-flash",
    description="An agent that summarizes text into short, clear summaries.",
    instruction="""
        You are a helpful text summarization assistant.
        When the user gives you any text, summarize it clearly and concisely in 3-5 sentences.
        Focus on the key points only.
    """,
    tools=\[summarize\_text],
)
```

**What each part does:**

* `from google.adk.agents import Agent` — imports the ADK tool
* `summarize\_text()` — a tool the agent can use
* `root\_agent` — the actual agent with its name, model, and instructions
* `model="gemini-2.5-flash"` — uses Google's Gemini AI to think
* `instruction` — tells the agent its personality and job

\---

### 2\. `summarizer\_agent/\_\_init\_\_.py`

Just one line. Tells Python this folder is a proper package.

```python
from . import agent
```

\---

### 3\. `summarizer\_agent/.env`

Your secret credentials. **Never upload this to GitHub!**

```
GOOGLE\_GENAI\_USE\_VERTEXAI=FALSE
GOOGLE\_API\_KEY=your\_api\_key\_here
```

Get your API key from: https://aistudio.google.com/apikey

\---

### 4\. `.env.example`

A safe template showing others what the `.env` file should look like:

```
# Copy this file, rename it to .env, and fill in your values

# Option 1: Gemini API Key
GOOGLE\_GENAI\_USE\_VERTEXAI=FALSE
GOOGLE\_API\_KEY=your\_gemini\_api\_key\_here

# Option 2: Vertex AI (Google Cloud)
# GOOGLE\_GENAI\_USE\_VERTEXAI=TRUE
# GOOGLE\_CLOUD\_PROJECT=your\_project\_id\_here
# GOOGLE\_CLOUD\_LOCATION=us-central1
```

\---

### 5\. `requirements.txt`

Lists the Python packages needed to run the agent:

```
google-adk
```

\---

## Live Endpoints

|Endpoint|Method|Description|
|-|-|-|
|`/health`|GET|Check if agent is running → `{"status":"ok"}`|
|`/list-apps`|GET|List available agents → `\["summarizer\_agent"]`|
|`/docs`|GET|Full API documentation|
|`/apps/{app}/users/{user}/sessions/{session}`|POST|Create a session|
|`/run\_sse`|POST|Run the agent and get a response|

\---

## How to Test the Live Agent

The agent works as an HTTP API. You need to:

1. First **create a session**
2. Then **call the agent**

### Step 1 — Create a session:


curl -X POST https://summarizer-agent-793500608148.us-central1.run.app/apps/summarizer\_agent/users/user1/sessions/session1 \\
  -H "Content-Type: application/json" \\
  -d "{}"


### Step 2 — Call the agent:


curl -X POST https://summarizer-agent-793500608148.us-central1.run.app/run\_sse \\
  -H "Content-Type: application/json" \\
  -d "{\\"app\_name\\":\\"summarizer\_agent\\",\\"user\_id\\":\\"user1\\",\\"session\_id\\":\\"session1\\",\\"new\_message\\":{\\"role\\":\\"user\\",\\"parts\\":\[{\\"text\\":\\"YOUR LONG TEXT HERE\\"}]}}"


### Expected Response:

```json
{
  "content": {
    "parts": \[{
      "text": "AI is transforming every industry, with companies investing billions in research. Despite this progress, concerns about job loss due to AI remain."
    }],
    "role": "model"
  }
}
```

> \*\*Windows users:\*\* Add `--ssl-no-revoke` after `curl` to avoid SSL errors.

\---

## 

## How to Run This Yourself (Step by Step)

### Prerequisites

* Windows PC
* Python 3.x installed (Anaconda recommended)
* Google Cloud account with billing enabled
* Docker Desktop installed

\---

### Step 1: Set up Google Cloud

1. Go to https://cloud.google.com and sign in
2. Create a new project (e.g. `genai-agent`)
3. Enable these APIs:

```bash
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable aiplatform.googleapis.com
```

\---

### Step 2: Install Google Cloud CLI

1. Download from: https://cloud.google.com/sdk/docs/install#windows
2. Run the installer, keep all defaults
3. Run `gcloud init` and sign in
4. Verify:

```bash
gcloud --version
```

\---

### Step 3: Create the project folder

Open Anaconda Prompt and run:

```bash
cd Desktop
mkdir genai-agent
cd genai-agent
mkdir summarizer\_agent
```

Install ADK:

```bash
pip install google-adk
```

\---

### Step 4: Create the files

Create these 4 files using Notepad:

```bash
notepad summarizer\_agent\\agent.py
notepad summarizer\_agent\\\_\_init\_\_.py
notepad summarizer\_agent\\.env
notepad requirements.txt
```

Paste the code shown in the File Explanations section above into each file.

Get your API key from: https://aistudio.google.com/apikey

\---

### Step 5: Test locally

```bash
adk web
```

Open browser at: `http://localhost:8000/dev-ui/`

Select `summarizer\_agent` from dropdown, type some long text → it will summarize it! ✅

Press `Ctrl+C` to stop.

\---

### Step 6: Deploy to Cloud Run

Make sure Docker Desktop is running, then set your project:

```bash
gcloud config set project YOUR\_PROJECT\_ID
```

Give permissions to the service account:

```bash
gcloud projects add-iam-policy-binding YOUR\_PROJECT\_ID --member="serviceAccount:YOUR\_PROJECT\_NUMBER-compute@developer.gserviceaccount.com" --role="roles/storage.objectAdmin"

gcloud projects add-iam-policy-binding YOUR\_PROJECT\_ID --member="serviceAccount:YOUR\_PROJECT\_NUMBER-compute@developer.gserviceaccount.com" --role="roles/cloudbuild.builds.builder"

gcloud projects add-iam-policy-binding YOUR\_PROJECT\_ID --member="serviceAccount:YOUR\_PROJECT\_NUMBER-compute@developer.gserviceaccount.com" --role="roles/artifactregistry.writer"
```

Deploy (all one line — no backslashes on Windows):

```bash
adk deploy cloud\_run --project=YOUR\_PROJECT\_ID --region=us-central1 --service\_name=summarizer-agent summarizer\_agent
```

When asked:

* "Continue?" → type `Y`
* "Allow unauthenticated invocations?" → type `y`

Wait 5-10 minutes. You'll see:

```
Service URL: https://summarizer-agent-XXXXXXXXX.us-central1.run.app
```

\---

### Step 7: Set environment variables on Cloud Run

```bash
gcloud run services update summarizer-agent --region=us-central1 --set-env-vars="GOOGLE\_GENAI\_USE\_VERTEXAI=FALSE,GOOGLE\_API\_KEY=your\_api\_key\_here"
```

\---

### Step 8: Verify it's live

Open these in your browser:

|URL|Expected Result|
|-|-|
|`/health`|`{"status":"ok"}`|
|`/list-apps`|`\["summarizer\_agent"]`|
|`/docs`|Full API documentation|

\---

## Common Errors \& Fixes

|Error|Fix|
|-|-|
|`RESOURCE\_EXHAUSTED`|API key quota exceeded. Create a new key or enable billing|
|`404 model not found`|Update model name to `gemini-2.5-flash`|
|`Access Denied` on deploy|Run Anaconda Prompt as Administrator|
|`Permission denied` on Cloud Run|Add IAM roles to service account (see Step 6)|
|`push rejected` on git|Run `git push -u origin main --force`|
|`\\` backslash error on Windows|Put entire command on one line, no backslashes|
|`Session not found`|Always create a session first before calling `/run\_sse`|
|`403 PERMISSION\_DENIED` on Cloud Run|Set env vars using `gcloud run services update --set-env-vars`|
|`detail: Not Found` on root URL|Normal! Use `/health`, `/docs`, or `/run\_sse` instead|

\---

## How the Agent Works

```
User sends POST request with long text
              ↓
Agent receives the text via /run\_sse
              ↓
Creates a session to track the conversation
              ↓
Sends text to Gemini 2.5 Flash AI
              ↓
Gemini reads and summarizes it
              ↓
Agent returns summary in JSON response ✅
```

\---

## Security Notes

* Never upload your `.env` file to GitHub
* Always add `.env` to `.gitignore`
* Provide `.env.example` so others know what variables to set
* Regenerate your API key if it gets accidentally exposed
* Use `gcloud run services update --set-env-vars` to set secrets on Cloud Run

\---

## Author

**Yogita Kore**

* GitHub: [@YogitaKore791](https://github.com/YogitaKore791)
* Built as part of Google GenAI Academy Challenge

\---

## Resources

* [Google ADK Documentation](https://google.github.io/adk-docs/)
* [Gemini API Models](https://ai.google.dev/gemini-api/docs/models)
* [Cloud Run Documentation](https://cloud.google.com/run/docs)
* [Google AI Studio](https://aistudio.google.com)
* [GenAI Academy](https://vision.hack2skill.com/event/apac-genaiacademy)

