import socket
import os

# Configure these values according to your needs
SERVER_IP = 'localhost'
SERVER_PORT = 69
BUFFER_SIZE = 516
BLOCK_SIZE = 512

# Function to handle sending file to the client
def send_file(filename, mode, client_socket, client_address):
    print('Client requested the file: ' + filename)
    if os.path.isfile(filename):
        # Open the file in binary or text mode based on the mode specified in the request
        with open(filename, 'rb' if mode == 'octet' else 'r') as f:
            block = 1
            # Read and send the file block by block
            data = f.read(BLOCK_SIZE)
            while data:
                # Construct data packet
                data_packet = b''.join([bytes([0]), bytes([3]), bytes([block >> 8]), bytes([block & 0xff]), data])
                # Send data packet
                client_socket.sendto(data_packet, client_address)
                # Wait for acknowledgment
                ack = client_socket.recv(BUFFER_SIZE)
                # Check for correct ACK
                if len(ack) != 4 or ack[1] != 4 or ack[2] != block >> 8 or ack[3] != block & 0xff:
                    print('Error: Incorrect ACK')
                    return
                # Read next block
                data = f.read(BLOCK_SIZE)
                block += 1
        print('File sent successfully.')
    else:
        print('Error: File not found')

# Function to start the TFTP server
def start_tftp_server():
    # Create a UDP server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the specified IP and port
    server_socket.bind((SERVER_IP, SERVER_PORT))
    while True:
        # Receive data from the client
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        # Handle RRQ packets
        if len(data) >= 4 and data[1] == 1:
            # Extract filename and mode from the request
            filename = data[2:-1].decode('utf-8').split('\0')[0]
            mode = data[2:-1].decode('utf-8').split('\0')[1]
            # Send the requested file
            send_file(filename, mode, server_socket, addr)

if __name__ == '__main__':
    start_tftp_server()
