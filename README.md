# CTF_SSH

## Description
This Capture The Flag (CTF) challenge is designed for the IT Security course at Adolfo Ibáñez University for the first semester of 2024. It involves a mix of SSH access, network sniffing, code execution, and firewall manipulation techniques. Participants will need to leverage their skills in these areas to solve the challenge and capture the flag.

## Setup
### Prerequisites
- A machine with Docker installed. For installation instructions, refer to [Docker's official documentation](https://docs.docker.com/get-docker/).
- The Docker container needs to expose port 22 for SSH; however, since this port is typically used by the host's SSH server, you should map it to a different port on the host machine.

### Running the Challenge
1. **Build the Docker Image**:
   Clone the repository and navigate to the directory containing the Dockerfile.
   ```bash
   git clone <repository-url>
   cd <repository-path>
   ```
   Build the Docker image using:
   ```bash
   docker build -t ubuntu-ssh .
   ```
2. **Start the Docker Container**:
   Run the container:
   ```bash
   docker run -d --name my-ubuntu-ssh ubuntu-ssh
   ```
   This command starts the Docker container in detached mode and gives the container a name for easy reference.

## Accessing the Challenge
Participants can connect to the SSH server running in the Docker container using:
```bash
ssh ctfuser@<host-ip>
```
Replace <host-ip> with the IP address of the host machine. Use the credentials provided separately for ctfuser.

## Objective

The main objective of this challenge is to capture the flag hidden within the environment. This may involve breaking through several layers of security, executing code, exploiting vulnerabilities, and configuring or bypassing firewall settings.

## Rules

Do not attack the Docker host or other infrastructure.
Focus your efforts only on the intended challenge Docker container.
Sharing solutions with other participants is strictly prohibited.
Support

For any issues, questions, or needed clarifications regarding the challenge, please contact the course instructor or TA.

## Acknowledgments

Thanks to all contributors and the IT Security course staff for designing and testing this challenge.
