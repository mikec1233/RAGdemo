# Use a lightweight Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
# Since the build context is backend/, adjust the path to point to requirements.txt directly
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
# Since the build context is backend/, you can just copy everything
COPY . /app/backend

# Create necessary directories
RUN mkdir -p /app/backend/data/Chroma

# Expose the port for FastAPI
EXPOSE 8000

# Command to run FastAPI
CMD ["uvicorn", "backend.src.api.api_handler:app", "--host", "0.0.0.0", "--port", "8000"]

