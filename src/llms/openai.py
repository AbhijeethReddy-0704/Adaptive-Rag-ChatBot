"""
Anthropic Claude LLM initialization and configuration.
"""

import os

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()
os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY", "")

llm = ChatAnthropic(
    model="claude-sonnet-4-5",
    temperature=0
)