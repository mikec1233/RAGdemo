FROM public.ecr.aws/lambda/python:3.11

# Copy requirements.txt
COPY backend/requirements.txt ${LAMBDA_TASK_ROOT}

# Required to make SQLlite3 work for Chroma.
RUN pip install pysqlite3-binary

# Install the specified packages
RUN pip install -r requirements.txt --upgrade

# For local testing.
EXPOSE 8000

# Set IS_USING_IMAGE_RUNTIME Environment Variable
ENV IS_USING_IMAGE_RUNTIME=True

# Copy all relevant source files from the backend/src
COPY backend/src/app_logic ${LAMBDA_TASK_ROOT}/app_logic
COPY backend/src/database ${LAMBDA_TASK_ROOT}/database
COPY backend/src/api ${LAMBDA_TASK_ROOT}/api

# Copy Chroma data
COPY backend/Chroma ${LAMBDA_TASK_ROOT}/Chroma

# Copy any additional data files
COPY backend/data ${LAMBDA_TASK_ROOT}/data



