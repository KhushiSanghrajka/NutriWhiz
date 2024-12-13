# from langgraph.prebuilt import ToolExecutor
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI, OpenAI
from calorie_counter import calorie_counter
from recipe_data import recipe_agent
from recipe_generator_planner import recipe_generator_plan
from faq_answers import faq_answers
from flask import Flask, request, jsonify
from langgraph.graph import Graph
import os
import json

# Initialize Flask app
app = Flask(__name__)
OPENAI_API_KEY = os.getenv("OPENAI_KEY")

tools=[calorie_counter, recipe_agent, recipe_generator_plan, faq_answers]
model_With_tools = ChatOpenAI(base_url="https://models.inference.ai.azure.com", model="gpt-4o", api_key=OPENAI_API_KEY).bind_tools(tools)
tool_node = ToolNode(tools)

@app.route("/ask", methods=["POST"])
def ask_agent():
    data = request.json
    query = str(data.get("query"))
    if not query:
        return jsonify({"error": "Query is required"}), 400

    try:
        response = tool_node.invoke({"messages": [model_With_tools.invoke(query)]})
        print("RES:::", response)
        return jsonify({"response": json.loads(response['messages'][0].content)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()
