# Use the official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code and config file
COPY app.py app.py
COPY config.json config.json

# Expose the port the Flask app runs on
EXPOSE 5000

# The command to run the application
# We use host='0.0.0.0' to make the app accessible from outside the container
CMD ["flask", "run", "--host=0.0.0.0"]