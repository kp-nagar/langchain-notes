
from langchain.chat_models import init_chat_model
import os

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = "lsv2_p..."
os.environ["LANGSMITH_PROJECT"] = "pr-candid-latex-61"


os.environ["GROQ_API_KEY"] = "gsk_6..."
model = init_chat_model("llama3-8b-8192", model_provider="groq")

result = model.invoke("Hello, world!")
print(result)