import getpass
import os
from langchain.chat_models import init_chat_model
from langchain.chains.combine_documents import create_stuff_documents_chain


# if not os.environ.get("GROQ_API_KEY"):
#   os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

os.environ["GROQ_API_KEY"] = "gsk_6..."
model = init_chat_model("llama3-8b-8192", model_provider="groq")

s = model.invoke("Hello, world!")
print(s)