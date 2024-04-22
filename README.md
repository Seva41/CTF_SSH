# CTF_SSH

## Description
This Capture The Flag (CTF) challenge is designed for the IT Security course at Adolfo Ibáñez University for the first semester of 2024. It involves a mix of SSH access, network sniffing, code execution, and firewall manipulation techniques. Participants will need to leverage their skills in these areas to solve the challenge and capture the flag.

## Setup
### Prerequisites
- A machine with Docker installed. For installation instructions, refer to [Docker's official documentation](https://docs.docker.com/get-docker/).
- Ensure that Docker is configured to allow non-root users to execute Docker commands. This can be achieved by adding the user to the `docker` group:
  ```bash
  sudo usermod -aG docker $USER
  ```
  Log out and back in for this change to take effect.
- The machines used by the participants should have a rule of `iptables-persistent` blocking the IP of the Docker machine. This would prevent the connection using SSH, as well as being a hint to them to guess the IP they need to connect to:
  ```bash
  sudo apt install iptables-persistent
  iptables -A OUTPUT -p tcp --dport 22 -d <ip_address> -j REJECT
  iptables-save > /etc/iptables/rules.v4
  ```
  Be sure to replace `<ip_address>` with the right IPv4 of the Docker machine.
  
### Running the Challenge
1. **Clone the Repository**:
   Clone the repository to get the Dockerfile and any other necessary files.
   ```bash
   git clone https://github.com/Seva41/CTF_SSH
   cd CTF_SSH
   ```

2. **Build the Docker Image**:
   Build the Docker image using the Dockerfile in the cloned repository.
   ```bash
   docker build -t ubuntu-ssh .
   ```

3. **Start the Docker Container**:
   Run the container:
   ```bash
   docker run -d --name my-ubuntu-ssh ubuntu-ssh
   ```
   This command starts the Docker container in detached mode and names the container for easy reference.

## Shell Script for Setup
Participants can utilize a shell script to automate the setup process. The script will build and run the Docker container and handle any necessary preliminary setup.
```bash
#!/bin/bash

# Build the Docker image
docker build -t ubuntu-ssh .

# Run the Docker container
docker run -d --name my-ubuntu-ssh ubuntu-ssh

echo "Container is set up and running. You can SSH using: ssh ctfuser@<host-ip>"
```
This script should be saved as a .sh file in a suitable directory, such as:
```bash
/usr/local/bin/
```
And be executable:
```bash
sudo chmod +x /usr/local/bin/launch_container_script.sh
```

Then the script should be called when a SSH connection is made. For this, modify the SSH configuration:
```bash
sudo nano /etc/ssh/sshd_config
```
by adding at the end of the file:
```bash
Match User ctfuser
    ForceCommand /usr/local/bin/launch_container_script.sh
```

## Objective
The main objective of this challenge is to capture the flag hidden within the environment. This may involve breaking through some layers of security, executing code, inspecting network capture files, and configuring or bypassing firewall settings.

## Rules
- Do not attack the Docker host or other infrastructure.
- Focus your efforts only on the intended challenge Docker container.
- Sharing solutions with other participants is strictly prohibited.

## Support
For any issues, questions, or needed clarifications regarding the challenge, please contact me.

