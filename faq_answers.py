import os
from langchain_community.tools import TavilySearchResults
from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAI
from langchain_core.runnables import RunnableConfig, chain
from langchain_core.tools import tool

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
    llm = ChatOpenAI(base_url="https://models.inference.ai.azure.com", model="gpt-4o", openai_api_key='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')

    # TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    # tool = TavilySearchResults(
    #     max_results=3,
    #     search_depth="advanced",
    #     include_answer=True,
    # )

    # llm_with_tools = llm.bind_tools([tool])

    llm_chain = prompt | llm

    answer = llm_chain.invoke(query, return_only_outputs=True)
    print("ANSWER:::",answer)
    response = answer
    # @chain
    # def tool_chain(user_input: str, config: RunnableConfig):
    #     input_ = {"query": user_input}
    #     ai_msg = llm_chain.invoke(input_, config=config)
    #     tool_msgs = tool.batch(ai_msg.tool_calls, config=config)
    #     result = llm_chain.invoke({**input_, "messages": [ai_msg, *tool_msgs]}, config=config)
    #     print("Result", result)
    #     print(type(result))
    #     print(result.content)
    #     return result.content


    # result = result['messages']
    # ans = answer['response'][0].content
    # print("ANS:::",type(ans))
    return {"response":response}

# ans = faq_answers("What is the best diet for weight loss?")
# print(ans['response'][0].content)
