from langchain_core.tools import tool
import os
from langchain.chat_models import init_chat_model

@tool()
def multiply_my_number(a: int, b: int) -> int:
    """
    Multiply a and b.
    Args:
        a: first int
        b: second int
    """
    return a * b

os.environ["GROQ_API_KEY"] = "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"
model = init_chat_model("llama3-8b-8192", model_provider="groq")

tool_model = model.bind_tools([multiply_my_number])

response = tool_model.invoke("how much water in ocean?")
print(response)

# Now, manually execute the tool call
# tool_call = response.tool_calls[0]  # Get first tool call
# tool_result = multiply_my_number.invoke(tool_call["args"])
# # Print the result
# print(f"Tool result: {tool_result}")