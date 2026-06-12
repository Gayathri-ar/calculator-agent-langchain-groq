from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

load_dotenv()

# LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b"
)

# Calculator Tool
@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    Example: 25*18, (100+50)/5
    """
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

# Create Agent
agent = create_react_agent(
    llm,
    tools=[calculator]
)

while True:
    question = input("\nAsk a question (or exit): ")

    if question.lower() == "exit":
        break

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    print("\nAnswer:")
    print(response["messages"][-1].content)