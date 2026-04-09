"""
ReAct agent setup for document retrieval and question answering.
"""

from langgraph.prebuilt import create_react_agent

from src.llms.openai import llm
from src.rag.retriever_setup import get_retriever


def get_agent_executor():
    """
    Create a ReAct agent with the current retriever tool.

    Called on every retrieval to ensure the agent always uses the
    latest vectorstore (updated after each document upload).

    Returns:
        A compiled LangGraph ReAct agent with the current retriever.
    """
    return create_react_agent(llm, [get_retriever()])
