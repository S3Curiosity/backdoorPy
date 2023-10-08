# Remote Shell Script

This is a Python script that allows you to establish a remote shell connection to a target machine over a network. You can execute commands on the target machine and perform file uploads and downloads.

## Prerequisites

Before using this script, make sure you have the following:

- Python installed on both the host and target machines.
- Basic knowledge of networking and IP addresses.

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the directory where you saved the script.

3. Run the script with the following command, replacing `<ip_address>` and `<port>` with the appropriate values:
   
   ```shell
   python serverBackDoor.py <ip_address> <port>

----------------------------------------------------------------------------------------------------------------

# Remote Control Script  - backDoor.py

A Python script for remote control and data exchange between a client and server using sockets. This script allows you to establish a connection to a remote server and execute commands on the server, upload and download files, and receive command results.

## Prerequisites

- Python 3.x
- A remote server with the server script running

## Configuration

Before using the script, make sure to configure the following parameters in the script:

- `SERVER_IP`: The IP address of the remote server.
- `SERVER_PORT`: The port on which the server is listening.

## Usage

1. Ensure that the server script is running on the remote server.

2. Run the `remote_control.py` script on your local machine.

3. The script will attempt to connect to the remote server using the configured IP address and port.

4. Once connected, you can use the following commands in the client shell:

    - `quit`: Terminate the connection and exit the client.
    - `clear`: Clear the screen on the server (currently not implemented in the script).
    - `cd <directory>`: Change the current working directory on the server.
    - `download <file_name>`: Download a file from the server to the client.
    - `upload <file_name>`: Upload a file from the client to the server.
    - Any other command: Execute the command on the server and receive the output.

## Troubleshooting

If you encounter any connection issues, make sure that the server is running and that the `SERVER_IP` and `SERVER_PORT` parameters in the script are correctly configured.

## License

This script is licensed under the [MIT License].

## Disclaimer

Please use this script responsibly and ensure that you have the right to test the target in question.

The authors and contributors of this script are not responsible for any misuse or legal consequences that may arise from its use.
