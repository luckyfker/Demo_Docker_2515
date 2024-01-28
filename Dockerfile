# Use a base image with Python and Alpine Linux
FROM python:3.8-alpine

# Install required libraries
RUN apk add --no-cache build-base linux-headers
RUN pip install python-can

# Set the working directory
WORKDIR /app

# Copy the Python script into the container
COPY pi_can_communication.py /app/pi_can_communication.py

# Run the Python script
CMD ["python", "pi_can_communication.py"]
