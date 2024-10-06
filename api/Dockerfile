FROM python:3.11

WORKDIR /code

# Copy requirements and install dependencies
COPY ./requirements-api.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code
COPY ./app /code/app

# Download wait-for-it.sh script to wait for OpenSearch to be ready
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /code/wait-for-it.sh
RUN chmod +x /code/wait-for-it.sh

# Expose the FastAPI port
EXPOSE 80

# Run the create_index.py script and then start FastAPI using uvicorn
CMD ["/code/wait-for-it.sh", "opensearch:9200", "--timeout=60", "--", "python", "/code/app/create_index.py", "&&", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
