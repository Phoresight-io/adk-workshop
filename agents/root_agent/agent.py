from google.adk.agents import Agent

from .tools import get_current_time, search_web

root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="A general-purpose root agent that can answer questions and use tools.",
    instruction=(
        "You are a helpful AI assistant. "
        "Use the available tools to answer user questions accurately and concisely. "
        "When you are unsure, say so rather than guessing."
    ),
    tools=[get_current_time, search_web],
)
