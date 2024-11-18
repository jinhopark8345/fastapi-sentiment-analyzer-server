from python:3.10-slim-bookworm

# Set the working directory inside the container
WORKDIR /app


# Install PyTorch and any additional dependencies
RUN pip install --no-cache-dir torch==2.5.1
RUN pip install sqlalchemy

# Install any necessary Python dependencies from requirements.txt
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the models directory into the container
COPY models models

# Copy the current directory contents into the container
COPY . /app

# Install the project
RUN pip install .

# Expose the port your app will run on (default is 8000 for FastAPI, adjust as needed)
EXPOSE 8081

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]
