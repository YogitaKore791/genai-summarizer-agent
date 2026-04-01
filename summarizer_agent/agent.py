from google.adk.agents import Agent

def summarize_text(text: str) -> str:
    """Summarizes the given text into a short, clear summary."""
    return text

root_agent = Agent(
    name="summarizer_agent",
    model="gemini-2.5-flash",
    description="An agent that summarizes text into short, clear summaries.",
    instruction="""
        You are a helpful text summarization assistant.
        When the user gives you any text, summarize it clearly and concisely in 3-5 sentences.
        Focus on the key points only.
    """,
    tools=[summarize_text],
)