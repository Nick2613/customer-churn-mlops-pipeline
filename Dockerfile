# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Create directories (in case they don't exist)
RUN mkdir -p data logs reports

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the main pipeline
CMD ["python", "main_pipeline.py"]
