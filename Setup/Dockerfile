# Use an official Ubuntu base image
FROM ubuntu:latest

# Install SSH server and utilities
RUN apt-get update && apt-get install -y openssh-server sudo

# Setup necessary files and permissions for SSH
RUN mkdir /var/run/sshd
RUN echo 'root:YOUR_SECURE_PASSWORD' | chpasswd  # Consider setting a secure password for root as well
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Create a non-root user with the username 'ctfuser' and create a group 'ctfuser'
RUN groupadd ctfuser && useradd -m -s /bin/bash -g ctfuser -G sudo ctfuser
RUN echo 'ctfuser:YOUR_SECURE_PASSWORD' | chpasswd

# SSH login fix to prevent disconnection after login
RUN sed -i 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' /etc/pam.d/sshd

# Create directories
RUN mkdir -p /home/ctfuser/Desktop /home/ctfuser/Documents /home/ctfuser/Downloads

# Create a TXT file on the Desktop named 'flag.txt'
RUN echo 'FLAG' > /home/ctfuser/Desktop/flag.txt

# Change owner of the home directory to 'ctfuser'
RUN chown -R ctfuser:ctfuser /home/ctfuser

