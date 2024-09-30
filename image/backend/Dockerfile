FROM public.ecr.aws/lambda/python:3.11

# Install SQLite3 from source
RUN yum install -y wget tar gzip gcc make \
    && wget https://www.sqlite.org/2023/sqlite-autoconf-3410200.tar.gz \
    && tar xvfz sqlite-autoconf-3410200.tar.gz \
    && cd sqlite-autoconf-3410200 \
    && ./configure \
    && make \
    && make install \
    && cd .. \
    && rm -rf sqlite-autoconf-3410200 sqlite-autoconf-3410200.tar.gz

# Copy requirements.txt first to leverage Docker caching for dependencies
COPY requirements.txt /var/task/requirements.txt

# Required to make SQLite3 work for Chroma.
RUN pip install pysqlite3-binary

# Install the specified packages
RUN pip install -r requirements.txt --upgrade

# For local testing.
EXPOSE 8000

# Set IS_USING_IMAGE_RUNTIME Environment Variable
ENV IS_USING_IMAGE_RUNTIME=True

# Copy the rest of the application files
COPY . /var/task/backend/

# Add /var/task/backend to PYTHONPATH
ENV PYTHONPATH="/var/task/backend"
