from langchain.llms.openai import OpenAI
from langchain.tools import StructuredTool
from langchain.agents import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent
from src.gpt.text_generator import request_chat_completion
from src.config import Config

def classify_text(text: str) -> str:
    """Classify text into one of three categories: meme, propaganda, marketing."""
    if not isinstance(text, str):
        raise TypeError("Text must be a string.")

    # Use gpt to classify 
    gpt_str = "Classify this text into one of three categories: meme, propaganda, marketing. \"" + text + "\". Response should be one of the three categories."
    result = request_chat_completion(previous_message={}, message=gpt_str)

    return "Classify this text into one of three categories: meme, propaganda, marketing. \"" + result + "\". Response should be one of the three categories."

tools: list[StructuredTool] = [
    StructuredTool.from_function(
        name= "Classify Text", 
        func=classify_text, 
        description="Classify text into one of three categories: meme, propaganda, marketing.",
    ),
]

# Make a memory for the agent to use
memory = ConversationBufferMemory(memory_key="chat_history")

llm = OpenAI(temperature=0, openai_api_key=Config().API_KEY)
agent_chain = initialize_agent(
    tools, 
    llm, 
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True, 
    memory=memory,
    max_iterations=10,
    )

def run_agent(prompt: str) -> str:
    """Run the agent."""
    if not isinstance(prompt, str):
        raise TypeError("Prompt must be a string.")

    if (len(prompt) < 1) or (len(prompt) > 1000):
        raise ValueError("Prompt must be at least 1 character or less than 1000 characters.")
    
    result = agent_chain.run(prompt)
    # logger.info(f"Finished running langchain_function_calling.py, result: {result}")
    return result

def main():
    """Run the agent."""
    prompt = input("Prompt: ")
    result = run_agent(prompt)
    print(f"Result: {result}")

# main()
# if __name__ == "__main__":
#     main()