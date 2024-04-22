# Solution

## Program execution
To be able to solve the challenge, the players must execute the 'captura' program:
```bash
sudo chmod +x captura
./captura
```
This will create a randomized `.pcap` file with a mix of different packets, such as DNS, TCP, ICMP, etc.

## Sniffer
The file must be opened using a sniffer program such as Wireshark.
Between the TCP packets, there will be 3 different, larger ones with some fictional credentials on their data. 2 of them are distractors, and the remaining one is the correct to use in a SSH connection to the machine running the Docker container.
The data can be recovered by identifying this packets, and following their TCP Stream in ASCII.

## SSH Connection
Participants can connect to the SSH server running in the Docker container using the following command:
```bash
ssh ctfuser@<host-ip>
```
Replace `<host-ip>` with the IP address of the host machine. Use the credentials provided separately for `ctfuser`, recovered in the `.pcap` file.

## Linux commands
With access to the container machine, the participants should be able to use `ls` to see the contents of the root directory, containing 3 folders. One of them, `Desktop`, contains the flag inside a file named `flag.txt`.
The users should be able to move to the directory and see the contents of the file using:
```bash
cd Desktop/
cat flag.txt
```
Then, the flag would be displayed to the user.
