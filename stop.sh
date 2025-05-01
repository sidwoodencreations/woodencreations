#!/bin/bash

echo "Stopping container 'app-container'..."
if docker ps -q --filter "name=app-container" | grep -q .; then
    docker stop app-container
    echo "Container stopped."
else
    echo "No running container named 'app-container' found."
fi

echo "Removing container 'app-container'..."
if docker ps -a -q --filter "name=app-container" | grep -q .; then
    docker rm app-container
    echo "Container removed."
else
    echo "No container named 'app-container' found."
fi


echo "Removing image 'my-app-image'..."
if docker images -q my-app-image | grep -q .; then
    docker rmi my-app-image
    echo "Image removed."
else
    echo "No image named 'my-app-image' found."
fi

echo "Cleanup completed."