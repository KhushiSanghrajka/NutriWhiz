from langchain_core.tools import tool

from langgraph.prebuilt import ToolNode

@tool
def calorie_counter(age: int, weight: float, height: float, activity_level: str, gender: str) -> dict:
    """
    Calculates the daily caloric intake based on age, weight, height, activity level, and gender.
    """
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9,
    }

    if activity_level not in activity_multipliers:
        return {"error": "Invalid activity level. Choose from 'sedentary', 'light', 'moderate', 'active', 'very active'."}

    if gender.lower() == "male":
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    elif gender.lower() == "female":
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
    else:
        return {"error": "Invalid gender. Choose 'male' or 'female'."}

    daily_caloric_intake = bmr * activity_multipliers[activity_level]

    return {
        "BMR": round(bmr, 2),
        "Daily Caloric Intake": round(daily_caloric_intake, 2),
    }
