from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
from dotenv import load_dotenv
load_dotenv()

model = ChatOllama(model='llama3.1')

schema=[
    ResponseSchema(name="fact1",description="Fact 1 about the topic"),
    ResponseSchema(name="fact2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact3", description="Fact 3 about the topic"),
]

parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template="Give 3 facts about the {topic}. \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

chain= template | model | parser

result=chain.invoke({'topic': "black Hole"})

print(result)