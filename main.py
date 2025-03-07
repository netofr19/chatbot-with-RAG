from dotenv import load_dotenv
from langchain_openai import OpenAI


load_dotenv()

llm_model = OpenAI()

pergunta = "Fale sobre a história do time Liverpool"
print(llm_model.invoke(pergunta))
