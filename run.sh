#!/bin/bash

# Build the Docker image
echo "Building Docker image..."
docker build -t my-app-image .

# Check if the build was successful
if [ $? -eq 0 ]; then
    echo "Docker image built successfully."

    echo "Running Docker container..."
    docker run -d -p 8080:80 --name app-container my-app-image

    # Check if the container started successfully
    if [ $? -eq 0 ]; then
        echo "Container 'app-container' is running"
    else
        echo "Failed to start the container."
        exit 1
    fi
else
    echo "Failed to build the Docker image."
    exit 1
fi