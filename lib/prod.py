import socket
from concurrent.futures import ThreadPoolExecutor
import atexit
from collections import deque

class SocketWrapper:
    class Stdin:
        def __init__(self, sock: socket.socket, chunk_size: int = 1024):
            self.socket = sock
            self.buffer = deque()
            self.chunk_size = chunk_size

        def readline(self):
            parts = list(self.buffer)
            while True:
                part = self.socket.recv(self.chunk_size).decode('utf8')
                if len(part) == 0:
                    # EOF
                    if len(parts) > 0:
                        return ''.join(parts)
                    return ''

                split_part = part.split('\n')
                if len(split_part) == 1:
                    # no newlines yet
                    parts.append(part)
                    continue

                if len(parts) > 0:
                    parts.append(split_part[0])
                    whole_part = ''.join(parts)
                    self.buffer.append(whole_part)
                    self.buffer.extend(split_part[1:])
                    return self.buffer.popleft()

                self.buffer.extend(split_part)
                return self.buffer.popleft()

    class Stdout:
        def __init__(self, sock: socket.socket):
            self.socket = sock

        def write(self, message: str):
            return self.socket.sendall(bytes(message, 'utf8'))

        def flush(self):
            return None


    def __init__(self, sock: socket.socket, chunk_size: int = 1024):
        self.stdin = self.Stdin(sock, chunk_size)
        self.stdout = self.Stdout(sock)
    

def answer_request(main, connection, address):
    print(f'Client connected from {address[0]}:{address[1]}')
    stdio_wrapper = SocketWrapper(connection)
    try:
        main(stdio_wrapper.stdin, stdio_wrapper.stdout)
    except Exception as e:
        print(f'[CRITICAL] encountered error at main: {e}')
    finally:
        connection.close()

def run_prod(config, main):
    pool = ThreadPoolExecutor(10)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((config.CTFNC_BIND, config.CTFNC_PORT))
    sock.listen()
    atexit.register(sock.close)
    print(f'Running in production at port {config.CTFNC_BIND}:{config.CTFNC_PORT}')
    while True:
        conn, addr = sock.accept()
        pool.submit(answer_request, main, conn, addr)
