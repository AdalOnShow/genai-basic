from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.8)
messages = []

print("------------------------Welcome! type 0 to exit chat------------------------")
while True:
    question = input("You : ")
    messages.append(question)
    if question == "0":
        print("Thank you for using our chatbot!")
        break
    response = model.invoke(messages)
    messages.append(response.content)
    print("Bot : ", response.content)

print(messages)
