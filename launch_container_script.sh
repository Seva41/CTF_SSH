#!/bin/bash

# Generate a unique container name with date and a random number
CONTAINER_NAME="ssh-session-$(date +%s)-$RANDOM"

# Start a new Docker container on a specified network and check if it started successfully
docker run -d --name "$CONTAINER_NAME" --network mynetwork ubuntu-ssh
if [ $? -ne 0 ]; then
    echo "Failed to start the container"
    exit 1
fi

# Give it a moment just in case the network is slow to assign an IP
sleep 5

# Retrieve the IP address of the newly created Docker container
CONTAINER_IP=$(docker inspect -f '{{.NetworkSettings.Networks.mynetwork.IPAddress}}' "$CONTAINER_NAME")
if [ -z "$CONTAINER_IP" ]; then
    echo "Failed to retrieve IP address for container $CONTAINER_NAME"
    echo "Attempting to remove the container..."
    docker rm -f "$CONTAINER_NAME"
    exit 1
fi

# Log the connection attempt
echo "Attempting to connect to $CONTAINER_IP with container $CONTAINER_NAME"

# SSH into the new container, forwarding the session handling
ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ctfuser@$CONTAINER_IP

# Clean up explicitly after SSH session ends
echo "Cleaning up container $CONTAINER_NAME..."
docker stop "$CONTAINER_NAME"
docker rm "$CONTAINER_NAME"
