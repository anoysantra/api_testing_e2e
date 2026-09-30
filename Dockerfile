# Use an official lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your automation suite files
COPY . .

# Run the pytest suite automatically when the container runs
CMD ["pytest", "-q"]

