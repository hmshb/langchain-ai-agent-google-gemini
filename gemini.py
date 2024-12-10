# LangChain + Google Gemini AI Integration Example
# Author: Hassan Mehmood
# Demonstrates how to have a class template for google gemini ai model integration with langchain

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate


class GoogleGeminiModel:
    def __init__(self):
        """Load environment variables and initialize the model."""
        self.load_environment_variables()
        self.llm = self.initialize_model()

    def load_environment_variables(self):
        """Load environment variables from the .env file."""
        load_dotenv()
        print("🔑 Loading API Key...")

        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("❌ Missing Google Gemini API key. Please set it in the .env file.")

        print("✅ API Key Loaded Successfully.")

    def initialize_model(self):
        """Initialize the Google Gemini model."""
        print("🤖 Initializing the Google Gemini Model...")
        llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=self.api_key)
        print("✅ Model Initialized Successfully.")
        return llm

    def execute_chain(self, prompt_template, input_text, input_variables):
        """Execute the chain with the provided prompt template and input."""
        print("📝 Setting up the Prompt Template...")

        # Create the prompt template
        prompt = PromptTemplate(input_variables=input_variables, template=prompt_template)

        print("🔗 Creating the LLM Chain...")

        # Combine the LLM and the prompt template into a chain
        chain = prompt | self.llm

        print("✅ Chain Setup Complete.")

        # Execute the chain and return the response
        print(f"📤 Sending the request to the Gemini AI Model...")
        response = chain.invoke(input=input_text)

        print("✅ Response Received.")
        return response.content