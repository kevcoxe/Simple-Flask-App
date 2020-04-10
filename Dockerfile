# Use the Python3.7.2 image
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
COPY . /app

# Install the dependencies
RUN pip install -r requirements.txt
RUN python init_db.py

ENTRYPOINT ["python"]

# run the command to start uWSGI
CMD ["app.py"]
