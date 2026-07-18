from models.llm import llm

response = llm.invoke("Hello! Introduce yourself in 3 lines.")

print(response.content)