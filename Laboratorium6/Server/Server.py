#Autor: Marcin Wawszczak 235274
#Program na Labolatorium 5 Systemów Wbudowanych

import math
import operator
import socket

#Kalkulator RPN wzorowany na repozytorium znalezionym w internecie
operators = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv,
       '^': operator.pow,
       'sin': math.sin,
       'tan': math.tan,
       'cos': math.cos,
       'pi': math.pi}

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

def calculate(equation):
    stack = []
    result = 0
    for i in equation:
        if is_number(i):
            stack.insert(0, i)
        else:
            if len(stack) < 2:
                print("Error: insufficient values in expression")
                break
            else:
                print("stack: %s" % stack)
                if len(i) == 1:
                    n1 = float(stack.pop(1))
                    n2 = float(stack.pop(0))
                    result = operators[i](n1, n2)
                    stack.insert(0, str(result))
                else:
                    n1 = float(stack.pop(0))
                    result = operators[i](math.radians(n1))
                    stack.insert(0, str(result))
    return result


def server():
    #konfiguracja hosta
    host = socket.gethostname()
    port = 5000
    
    server_socket = socket.socket()
    server_socket.bind((host, port))
    #Nasluch clienta
    server_socket.listen(2)
    conn, address = server_socket.accept()

    print("From: " + str(address))
    #Obsluga klienta
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print("From user: " + str(data))

        equation = str(data).split(' ')
        answer = calculate(equation)

        print("Answer: ")
        print(answer)
        aswerStr = "Answer: " + str(answer)
        data = aswerStr

        conn.send(data.encode())

    #Zakoncz polaczenie
    conn.close()


if __name__ == '__main__':
    server()