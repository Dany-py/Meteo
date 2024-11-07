FROM python:3.12

# Set the working directory
WORKDIR /workspace

# Copy the project files into the container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port for Django
EXPOSE 8000
