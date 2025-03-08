# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8501 for the Streamlit app
EXPOSE 8501

# Define environment variable
ENV STREAMLIT_SERVER_HEADLESS=true

# Run Streamlit app when the container starts
CMD ["streamlit", "run", "app/main.py", "--server.address=0.0.0.0", "--server.port=8501"]
