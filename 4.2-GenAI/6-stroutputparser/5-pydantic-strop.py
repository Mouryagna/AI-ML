from langchain_ollama import ChatOllama
from pydantic import BaseModel,Field
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
load_dotenv()

model = ChatOllama(model='llama3.1')

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int =Field(description="Age of the person",gt=18)
    city: str =Field(description="Name of the city where person belongs to")

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="generate the name, age, city of the fictional {place} person.\n {format_instructions}",
    input_variables=['place'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain= template | model | parser

result=chain.invoke({'place': "Indian"})

print(result)