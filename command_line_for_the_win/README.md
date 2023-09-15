# Command line for the win

## Using `sftp` to Upload Files to a Remote Server
___

This README provides a step-by-step guide on how I used `sftp` (SSH File Transfer Protocol) command to upload files from my local server to a remote server.

## Procedure

1. **Open a Terminal (Local Server):** Open a terminal or command prompt on your local server.

2. **Connect to the Remote Server:** Use the `sftp` command to establish an SSH connection to the remote server. Replace `username` with your remote server username and `hostname_or_ip` with the server's hostname or IP address. You will be prompted to enter your remote server password.

   ```bash
   sftp username@hostname_or_ip
   ```

3. **Navigate to the Destination Directory (Remote Server):** Once connected to the remote server via `sftp`, you'll see an `sftp>` prompt. Use the `cd` command to navigate to the directory on the remote server where you want to upload the files.

   ```bash
   cd remote_destination_directory
   ```

   Replace `remote_destination_directory` with the path to the destination directory on the remote server.

4. **Upload a File:** To upload a file from your local server to the remote server, use the `put` command followed by the path to the local file you want to transfer. Replace `local_file.txt` with the path to your local file.

   ```bash
   put local_file.png
   ```

   You will see progress information as the transfer occurs.

5. **Exit `sftp`:** To exit the `sftp` session and return to your local server's command prompt, type `exit` or `quit` at the `sftp>` prompt.
___

sftp> exit
