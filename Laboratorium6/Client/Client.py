#Autor: Marcin Wawszczak 235274
#Program na Labolatorium 5 Systemów Wbudowanych

import socket


def client():
    #konfiguracja klienta
    host = socket.gethostname()
    port = 5000
    #Nawiazywanie polaczenia
    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input(" -> ")
    #Komunikacja z serwerem
    while message.lower().strip() != 'logoff':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('From server: ' + str(data))
        message = input(" -> ")

    #Zakoncz polaczenie
    client_socket.close()


if __name__ == '__main__':
    client()
