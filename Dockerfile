# Use the official Python image from Docker Hub as a base image
FROM python:3.8-slim-buster

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Create and set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Run Flask when the container launches
CMD ["flask", "run"]
