# Offical Python runtime as parent image
FROM python:3.9-slim

# Sets the work directory in container to /app
WORKDIR /app

# Copying current directory contents in /app
COPY . /app

# installing requried libraries
RUN pip install --no-cache-dir -r requirements.txt uvicorn

# Expose the port the app runs on
EXPOSE 8000

# Runs app.py when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]