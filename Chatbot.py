# from: https://python.langchain.com/docs/integrations/llms/openai

# pip install langchain
# pip install openai

from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

from langchain.chains import APIChain
from langchain.chains.api import open_meteo_docs

llm = OpenAI(openai_api_key="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")

# template = """Question: {question}

# Answer: Let's think step by step."""

# prompt = PromptTemplate(template=template, input_variables=["question"])

# # Can make multiple chains, with multiple agents (need to figure out orchestration with multi-chains)
# llm_chain = LLMChain(prompt=prompt, llm=llm)

# question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

# result = llm_chain.run(question)

# print(result)

# Add context to the model
# Testing out API integrations


# llm = OpenAI(temperature=0) # Remove any ambiguity 

chain = APIChain.from_llm_and_api_docs(llm, open_meteo_docs.OPEN_METEO_DOCS, verbose=True)
chain.run('What is the weather like right now in Munich, Germany in degrees Fahrenheit?')

# chain.run('What is the weather like right now in Munich, Germany in degrees Celsius?')
