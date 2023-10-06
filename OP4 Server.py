import socket
import threading
import random

def handle_klient(client_socket):
    while True:
        request = client_socket.recv(1024).decode()
        if not request:
            break
        response = proc_req(request)
        client_socket.send(response.encode())
    client_socket.close()

def proc_req(request):
    parts=request.split(";")
    
    operation = parts[0]
    tal1=int(parts[1])
    tal2=int(parts[2])

    if operation=='Random':
        return str(random.randint(tal1,tal2))
    elif operation== 'Add':
        return str(tal1+tal2)
    elif operation =='Subtract':
        return str(tal1-tal2)
    else:
        return "Findes ikke"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 10))
server.listen(2)
print("Server is listening on port 10")

while True:
    client, addr =server.accept()
    print(f"Accept address from {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=handle_klient, args=(client,))
    client_handler.start()

