from langchain_core.tools import tool
from langchain_core.prompts.prompt import PromptTemplate
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
import os

OPENAI_API_KEY = os.getenv("OPENAI_KEY")

@tool
def recipe_generator_plan(query: str) -> dict:
    """
    Generates a meal plan or an instant recipe based on the user's query.
    """
    prompt_template = """
        You are an expert recipe generator and a weekly meal planner. Based on the user query, you have to decide whether to generate an instant recipe or a weekly meal plan.
            The input will be a natural language sentence, and the agent needs to extract the following key phrases and understand them:

            1. Preferences: The user may mention preferences such as:
                -Jain or non-Jain (e.g., "I want Jain recipes" or "Non-Jain meals").
                -Vegetarian, Non-Vegetarian, or Vegan (e.g., "Can you suggest vegan recipes?" or "I prefer vegetarian meals").
                
            2. Dietary Restrictions: The user may specify dietary restrictions such as:
                -Lactose Intolerance (e.g., "I'm lactose-intolerant, suggest meals accordingly").
                -Diabetic Friendly (e.g., "Diabetic-friendly recipes please").
                -Other dietary requirements like gluten-free, nut-free, etc.
            
            3. Calories: The user may mention a specific calorie requirement (e.g., "I need 1800 calories" or "Suggest a 2200-calorie meal plan").

            4. Meal Type: The user may specify the type of meal they are looking for:
                -Instant Recipe: If they want just one recipe (e.g., "Give me a recipe for dinner tonight").
                -Weekly Meal Plan: If they want a meal plan for the week (e.g., "Can you create a weekly meal plan for me?").

                If it is a meal plan, just generate a list of recipes for each day of the week. If it is an instant recipe, generate a single recipe.
            Here is the user query: {query}
        """
    
    prompt = PromptTemplate(input_variables=["query"], template=prompt_template)
    llm = ChatOpenAI(base_url="https://models.inference.ai.azure.com", model="gpt-4o", openai_api_key=OPENAI_API_KEY)

    recipe_chain = prompt | llm | StrOutputParser()
    result = recipe_chain.invoke(query, return_only_outputs=True)
    response = result

    return {"response": response}

# ans = recipe_generator_plan("Can you suggest a vegan recipe that's also diabetic-friendly and has 1800 calories?")
# print(ans)