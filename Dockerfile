FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy entire project files
COPY . .

# Expose port Django will run on
EXPOSE 8000

# Command to start Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
