
from langchain.chat_models import init_chat_model
import os

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = "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"
os.environ["LANGSMITH_PROJECT"] = "pr-candid-latex-61"


os.environ["GROQ_API_KEY"] = "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"
model = init_chat_model("llama3-8b-8192", model_provider="groq")

result = model.invoke("Hello, world!")
print(result)