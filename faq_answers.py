import os
from langchain_community.tools import TavilySearchResults
from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAI
from langchain_core.runnables import RunnableConfig, chain
from langchain_core.tools import tool
OPENAI_API_KEY = os.getenv("OPENAI_KEY")

@tool
def faq_answers(query: str) -> dict:
    """
    Answers frequently asked user queries related to diet and nutrition.
    """
    prompt_template = """
            Based on the user query, you have to answer the given question only if it is diet-related or nutritional-query related.
            Otherwise, you should just return 'I am unable to answer this at the moment'.
            Here is the user query: {query}
        """

    prompt = PromptTemplate(input_variables=["query"], template=prompt_template)
    llm = ChatOpenAI(base_url="https://models.inference.ai.azure.com", model="gpt-4o", openai_api_key=OPENAI_API_KEY)

    llm_chain = prompt | llm

    answer = llm_chain.invoke(query, return_only_outputs=True)
    print("ANSWER:::",answer)
    response = answer

    return {"response":response}
