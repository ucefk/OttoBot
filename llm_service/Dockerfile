# Use the official Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

RUN mkdir /Models/

RUN apt-get update && apt-get install
RUN apt-get install -y curl
RUN curl -fsSL https://ollama.com/install.sh | sh

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app directory to the container
COPY . /app

# Create a user and set permissions
RUN adduser --disabled-password --gecos "" appuser
RUN chown -R appuser:appuser /app

# Switch to the appuser
USER appuser

# Expose port 8883
EXPOSE 8883

# Set the environment variable
ENV OLLAMA_MODELS="/Models/"

# Set the command to run when the container starts
CMD ["uvicorn", "service:app", "--port", "8883"]
