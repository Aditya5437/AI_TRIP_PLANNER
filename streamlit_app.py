import streamlit as st
import requests

st.set_page_config(
    page_title="AI Trip Planner",
    page_icon="✈️",
    layout="centered"
)

st.title("✈️ AI Trip Planner")
st.write("Frontend Working")

st.markdown(
    "Plan trips using AI Agent + MCP + LangGraph"
)

user_query = st.text_input(
    "Enter your travel query"
)

if st.button("Generate Response"):

    if user_query:

        with st.spinner("Generating response..."):

            try:

                response = requests.post(

                    "http://127.0.0.1:8000/travel-planner",

                    json={
                        "query": user_query
                    }
                )

                result = response.json()

                st.success("Response Generated")

                st.write(result["response"])

            except Exception as e:

                st.error(f"Error: {e}")