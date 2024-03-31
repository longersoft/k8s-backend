# Use official Python image as the base image
FROM python:3.9-slim AS base

# Set working directory in the container
WORKDIR /app

# Copy only necessary files (requirements.txt and the Flask app) to the working directory
COPY requirements.txt ./
COPY main.py ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use a smaller image for final production
FROM python:3.9-slim AS final

# Set working directory in the container
WORKDIR /app

# Copy the built application and dependencies from the base stage
COPY --from=base /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=base /app ./

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=dev

# Expose the port on which the Flask app runs
EXPOSE 5000

# Command to run the Flask application
CMD ["flask", "run", "-p", "5000", "-h", "0.0.0.0"]
