import streamlit as st
import requests
import json

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://img.freepik.com/premium-photo/black-background-with-vegetables-blank-space-text_677426-316.jpg');
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Streamlit app title
st.markdown(
    """
    <h1 style='text-align: center; color: #FF5733;'>
        🥑 NutriWhiz 🥗
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown("<h3 style='text-align: center;'>Meals Made Right, Day and Night!</h3>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    textarea {
        color: #f9f9f9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Text input for the user query
query = st.text_area("Enter your query:", placeholder="What should be my calorie intake?")

# Button to submit the query
if st.button("Submit"):
    if not query.strip():
        st.error("Please enter a valid query.")
    else:
        st.info("Fetching response...")

        try:
            # Call the Flask backend API
            response = requests.post(
                "http://127.0.0.1:5000/ask", 
                json={"query": query}, 
                headers={"Content-Type": "application/json"}
            )

            if response.status_code == 200:
                data = response.json()
                if "error" in data:
                    st.error(f"Error: {data['error']}")
                else:
                    st.success("Response Received:")
                    st.json(data["response"])
            else:
                st.error(f"Failed to fetch response. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("""
**NutriWhiz** is your ultimate companion for all things nutrition and meal planning. With the power of AI, NutriWhiz helps you:
- Plan your meals based on your dietary preferences (Jain, vegetarian, vegan, etc.)
- Get personalized calorie intake recommendations
- Generate instant recipes
- Provide instant answers to nutrition-related FAQs
""")
# Footer for additional information
st.markdown("---")
st.caption("Helping you make better food choices, one meal at a time!")
