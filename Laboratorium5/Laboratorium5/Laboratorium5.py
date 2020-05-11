#Autor: Marcin Wawszczak 235274
#Program na Labolatorium 5 Systemów Wbudowanych

import http.client

url = http.client.HTTPSConnection("www.google.com")
url.request("GET", "/index.html")
response = url.getresponse()

file = open("response.txt","w")
file.write("Status: {} and reason: {}".format(response.status, response.reason))
file.close()

url.close()