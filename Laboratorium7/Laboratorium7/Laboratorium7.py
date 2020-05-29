#Autor: Marcin Wawszczak 235274
#Program na Labolatorium 7 Systemów Wbudowanych

import socket

def strona():
    if stan_obecny == 1:
        stan = "ON"
    else:
        stan = "OFF"

    html = """
    <html>
        <head> 
            <title>Symulowane urzadzenie</title> 
        </head>
        <body> 
            <h1> Symulowane urzadzenie</h1> 
            <p>Stan: """ + stan + """ </p>
            <p><a href="/?stan=on"><button class="on_button">ON</button></a></p> 
            <p><a href="/?stan=off"><button class="off_button">OFF</button></a></p>
        </body>
    </html>"""
    return html

#Fragment kodu na podstawie dokumentacji python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    c, a = s.accept()
    print('Connection from %s' % str(a))

    request = c.recv(1024)
    request = str(request)
    print('Content = %s' % request)

    device_on = request.find('/?stan=on')
    device_off = request.find('/?stan=off')

    stan_obecny = 0

    if device_on == 6:
        file = open('stan.txt', 'a+')
        file.write("ON\n")
        stan_obecny = 1
        file.close()

    if device_off == 6:
        file = open('stan.txt', 'a+')
        file.write("OFF\n")
        stan_obecny = 0
        file.close()

    response = strona()
    resp_bytes = response.encode('utf-8')

    c.sendall(resp_bytes)
    c.close()
