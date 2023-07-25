# Simple TFTP Server

This is a simple TFTP (Trivial File Transfer Protocol) server implementation in Python.

## How It Works

The server listens for requests on a specified IP address and port. When it receives a read request (RRQ) from a client, it opens the requested file and sends it to the client block by block. The server waits for an acknowledgment after each block it sends and stops when it has sent the entire file.

## Setup

1. Clone this repository to your local machine.

2. Run the server script:

    ```bash
    python3 tftp_server.py
    ```

3. The server will start listening for requests on the specified IP and port.

## Configuration

You can configure the server IP, port, and block size in the `tftp_server.py` file:

- `SERVER_IP`: The IP address that the server should listen on. Set this to `'localhost'` for testing on your local machine.

- `SERVER_PORT`: The port that the server should listen on. The standard TFTP port is 69, but you may need to run the script with sudo or as administrator to listen on this port. For testing, you can use any port number above 1024.

- `BLOCK_SIZE`: The size of each block of data that the server sends. The standard TFTP block size is 512 bytes.

## Limitations

This is a very basic implementation of a TFTP server. It only supports read requests and does not handle network errors or support simultaneous transfers to multiple clients. It's designed for educational purposes and not recommended for production use.

**Note**: Everything besides this note comment, from the first commit, has been created by a chatgpt prompt.

