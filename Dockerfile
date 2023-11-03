# Offical Python runtime as parent image
FROM python:3.9-slim

# Sets the work directory in container to /app
WORKDIR /app

# Copying crrent directory contents in /app
COPY . /app

# installing requried libraries
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Defining environment variables
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0


# Runs app.py when the container launches
CMD ["python", "app.py"]