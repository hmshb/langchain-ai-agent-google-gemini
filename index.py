# AI Agent with LangChain, Google Gemini, and DuckDuckGo
# Author: Hassan Mehmood
# Demonstrates how to create an AI Agent using the LangChain framework, 
# Google Gemini AI as a Large Language Model, and DuckDuckGo as a LangChain Search Tool.

from gemini import GoogleGeminiModel
from langchain_community.tools import DuckDuckGoSearchResults
from langchain.agents import Tool, initialize_agent


def main():
    # Initialize the Google Gemini Model
    gemini_model = GoogleGeminiModel()

    # Initialize the DuckDuckGo search tool
    search = DuckDuckGoSearchResults()

    # Define the tools for the agent
    tools = [
        Tool(
            name="Search",
            func=search.run,
            description="Search for information online."
        )
    ]

    # Initialize the agent using zero-shot-react-description mode
    agent = initialize_agent(
        tools=tools,
        llm=gemini_model.llm,
        agent_type="zero-shot-react-description"
    )

    # First question: Known answer from model's training data (should not use the tool)
    question = "What is the capital of France?"
    formatted_question = (
        f"{question} If you already know the answer from your training data, "
        "do not use any tools, just answer directly."
    )

    print(f"================== Question: {question} ====================\n")
    response = agent.invoke(formatted_question)
    print(f"================== Answer: {response['output']} \n")

    # Second question: Unknown answer, prompting the model to use the tool if needed
    question = "What is the next match of the Pakistan cricket team in 2025?"
    formatted_question = (
        f"{question} if you don't know the answer you can use the tool."
    )

    print(f"================== Question: {question} ====================\n")
    response = agent.invoke(formatted_question)
    print(f"================== Answer: {response['output']} \n")


if __name__ == "__main__":
    main()