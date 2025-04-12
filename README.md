# 🥑 NutriWhiz - AI Meal Planner & Nutrition Assistant 🥗

**NutriWhiz** is your ultimate companion for all things nutrition and meal planning. With the power of AI, NutriWhiz helps you:
- Plan your meals based on your dietary preferences (Jain, vegetarian, vegan, etc.)
- Get personalized calorie intake recommendations
- Generate instant recipes
- Provide instant answers to nutrition-related FAQs

---
## Inspiration
NutriWhiz was inspired by the everyday challenges faced by homemakers and individuals who struggle with meal planning and nutritional needs. Many of us find it difficult to decide what to cook every day, especially when we have limited ingredients at hand or specific dietary preferences. At the same time, balancing nutritional needs with the demands of a busy lifestyle can be overwhelming.

The idea behind NutriWhiz came from the desire to create a tool that could help simplify these tasks. By leveraging the power of AI, NutriWhiz assists users in generating meal plans, finding recipes that match available ingredients, and providing personalized calorie intake recommendations—all while considering dietary restrictions and preferences.

Whether it's helping someone stick to a vegan diet, finding the right meal for someone with diabetes, or simply suggesting a quick recipe with whatever ingredients are available, NutriWhiz was built to be a companion in the kitchen, making nutrition and meal planning effortless, efficient, and personalized.

NutriWhiz is not just about food; it's about empowering users with the right knowledge to make healthier choices and to navigate the complexities of modern nutrition with ease. It’s built with the intention of serving anyone who faces the common struggle of "What should I cook today?" in a way that is fun, easy, and tailored to their unique needs.

## Features

- **Calorie Intake Calculator**: Get personalized calorie intake recommendations based on your age, weight, height, activity level, and gender.
- **Meal Planner & Recipe Generator**: Generate meal plans for the week or one-time recipes to instantly satiate your cravings!
- **Dietary Preferences**: Supports Jain, vegetarian, vegan, and other dietary restrictions like lactose intolerance, diabetic-friendly meals, etc.
- **Nutrition FAQs**: Get instant answers to frequently asked questions related to diet and nutrition.

---

## Installation & Setup

### Prerequisites

Before running the app, ensure you have the following installed:

- Python 3.8 or higher
- `pip` package manager
- Virtual environment (optional but recommended)

### Steps to Install

1. **Clone the repository**

   ```bash
   git clone git@github.com:kevit-khushi-sanghrajka/NutriWhiz.git
   cd NutriWhiz
2. **Create a virtual environment (optional but recommended)**
    ```bash
    python -m venv venv
    source venv/bin/activate 
    # On Windows, use `venv\Scripts\activate`
3. **Change Branch**
    ```bash
    git checkout development
4. **Install required dependencies**
    ```bash
    pip install -r requirements.txt
5. **Run the app**
    ```bash
    python app.py
    streamlit run streamlit_app.py
6. Open your browser and navigate to http://localhost:8501 to use the app.

## Usage
Once the app is running, you can interact with NutriWhiz by entering queries like:

**Calorie Intake:** "What should be my calorie intake? I am a 25-year-old female, weighing 47kg, height is 166.75cm, and my activity level is moderate."<br><br>
**Meal Planning:** "Give me a vegan recipe for dinner tonight."<br><br>
**Dietary Restrictions:** "I need a meal plan for the week that's diabetic-friendly."<br><br>
**Nutrition Tips:** "What are some protein-rich foods for a plant-based diet?"<br><br>
NutriWhiz will process your query and provide responses accordingly.<br><br>

## Project Structure
```bash
nutriwhiz/
│
├── app.py              
    # Main file that runs the Streamlit app
├── calorie_counter.py  
    # Code for calorie intake calculator
├── recipe_data.py      
    # Recipe-related functionalities
├── recipe_generator_planner.py  
    # Code for generating meal plans and recipes
├── faq_answers.py      
    # FAQ-related functionalities
├── requirements.txt    
    # Python dependencies
└── README.md           
    # Project description
