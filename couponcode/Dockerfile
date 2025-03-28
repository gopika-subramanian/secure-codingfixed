# Use the official Python image as the base image
FROM python:2.7

# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install Flask and other dependencies
RUN pip install -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Start the Flask application
CMD ["flask", "run","--host", "0.0.0.0","--port","5000"]
