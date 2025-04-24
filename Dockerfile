# Use the official Python image
FROM python:3.11-slim

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy necessary files into the container
COPY requirements.txt ./
COPY .env.example ./
COPY run.py ./
COPY streamlit_app.py ./
COPY src/ ./src

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


