# Use the official Python base image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app

# Create a user and set permissions
RUN adduser --disabled-password --gecos "" appuser
RUN chown -R appuser:appuser /app

# Switch to the appuser
USER appuser

# Expose the port that Streamlit runs on
# EXPOSE 8501

# Set the entrypoint command to run the Streamlit app
ENTRYPOINT ["streamlit", "run", "app.py"]