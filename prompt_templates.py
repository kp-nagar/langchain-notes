from langchain_core.prompts import prompt, ChatPromptTemplate
import os
from langchain.chat_models import init_chat_model

prompt_template = prompt.PromptTemplate.from_template(
    """
    Tell me a joke about {topic}
    """
)

# prompt_template = ChatPromptTemplate([
#     ("system", "You are a helpful assistant"),
#     ("user", "Tell me a joke about {topic}")
# ])

# ask_prompt = prompt_template.invoke({"topic": "cats"})
# print(ask_prompt)

os.environ["GROQ_API_KEY"] = "gsk_6..."

model = init_chat_model("llama3-8b-8192", model_provider="groq")

chain = prompt_template | model

res = chain.invoke("cat")

print(res)
