from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Initialize the Groq LLM client
llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.8, max_tokens=20)

# Build a prompt template
prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant."), ("user", "{input}")]
)

# Create the chain and invoke it
chain = prompt | llm
response = chain.invoke({"input": "Hello! Give me a ai pome."})

print(response.content)
