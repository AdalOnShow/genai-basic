from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# 1. Load environment variables
load_dotenv()

# 2. Configure the endpoint with a distilled DeepSeek model and task
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
)

# 3. Wrap it in the Chat abstraction
model = ChatHuggingFace(llm=llm)

# 4. Invoke the model
response = model.invoke("Who are you?")
print(response.content)
