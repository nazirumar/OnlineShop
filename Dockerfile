# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /onlineshop

# Install dependencies and the gobject library
# Install dependencies and the libglib2.0-0 library
RUN apt-get update && \
    apt-get install -y \
    libglib2.0-0 \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libgdk-pixbuf2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /onlineshop/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . /onlineshop/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=myshop.settings

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
