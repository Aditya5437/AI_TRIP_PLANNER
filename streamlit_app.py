import streamlit as st
import requests
import time

st.set_page_config(
    page_title="AI Trip Planner",
    page_icon="✈️",
    layout="centered"
)

st.title("✈️ AI Trip Planner")

st.markdown(
    "Plan trips using AI Agent + MCP + LangGraph"
)

user_query = st.text_input(
    "Enter your travel query"
)

if st.button("Generate Response"):

    if user_query:

        with st.spinner("Generating response..."):

            response = None

            for attempt in range(3):

                try:

                    response = requests.post(

                        "https://ai-trip-planner-fai.onrender.com/travel-planner",

                        json={
                            "query": user_query
                        },

                        timeout=180
                    )

                    if response.status_code == 200:
                        break

                    time.sleep(5)

                except:
                    time.sleep(5)

            try:

                if response and response.status_code == 200:

                    result = response.json()

                    if "response" in result:

                        st.success("Response Generated")

                        st.write(result["response"])

                    elif "error" in result:

                        st.error(result["error"])

                    else:

                        st.error("Unknown backend response")

                else:

                    st.error(
                        f"Backend Error: {response.status_code}"
                    )

                    st.write(response.text)

            except Exception as e:

                st.error(f"Error: {e}")