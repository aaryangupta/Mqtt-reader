# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir gmqtt

# Expose the port for the MQTT broker if needed (optional, only if the broker runs inside this container)
EXPOSE 1883

# Define the command to run the application
CMD ["python", "newapp.py"]
