  
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 10))

for _ in range(3):

 operation = input("Enter operation (Random/Add/Subtract): ")
 num1 = input("Enter first number: ")
 num2 = input("Enter second number: ")

 request = f"{operation};{num1};{num2}"
 client.send(request.encode())

 response = client.recv(1024).decode()
 print(f"Server response: {response}")

client.close()

