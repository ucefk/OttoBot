import streamlit as st
import requests
import os
import logging
from dotenv import load_dotenv

# Load environment variables from the .env file (if present)
load_dotenv(".env")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get the prediction service name from an environment variable
# Use a default service name if the environment variable is not defined
MODEL_SERVICE = os.getenv("MODEL_SERVICE", "localhost")
MODEL_PORT = os.getenv("MODEL_PORT", "11434")
service_name = f"{MODEL_SERVICE}:{MODEL_PORT}"

logging.info(f"Model endpoin: {service_name}")

st.set_page_config(layout="wide")

st.title("OttoBot app")

options_column, chat_column = st.columns([1, 3])

# Check if the service is online
try:
    if requests.get(f"http://{service_name}/api/ps").status_code == 200:
        with options_column:
            st.write("🟢")
            
            models_list_response = requests.get(f"http://{service_name}/api/tags")
            models_list = models_list_response.json()

            # Extract model names using list comprehension
            model_names = [model["name"] for model in models_list["models"]]

            # Add a streamlit selector to choose the model
            # model_name = st.selectbox("Select model", model_names)
            model_name = st.radio(
                "Select the model to use: ",
                options=model_names,
            )

        with chat_column:
            # Get the question from the user
            question = st.chat_input(
                "Enter your question here",
            )

            # ask_button = st.button("Ask")

            if question and model_name:
                # Send the question to the prediction service
                response = requests.post(
                    f"http://{service_name}/api/generate", 
                    json={
                        "model": model_name,
                        "prompt": question,
                        "stream": False
                    }
                )

                # Display the written question
                st.markdown(f"Question: *{question}*")

                # Display the response
                st.write(response.json()["response"])

                # Log the question and response
                logging.info(f"Question: {question}")
                logging.info(f"Response: {response.json()['response']}")

    else:
        st.write("🔴")
        logging.error("Request failed. Response status code is not 200")
except requests.exceptions.RequestException as e:
    st.write("🔴🔴🔴")
    logging.critical(f"Service is offline. Error occurred: {e}")
