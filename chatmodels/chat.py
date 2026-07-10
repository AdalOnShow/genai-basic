import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Initialize the Groq LLM client
# Popular models include: llama3-8b-8192, llama3-70b-8192, mixtral-8x7b-32768
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.8)

# Build a prompt template
prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant."), ("user", "{input}")]
)

# Create the chain and invoke it
chain = prompt | llm
response = chain.invoke({"input": "Hello! Give me a 1-sentence productivity tip."})

print(response.content)
