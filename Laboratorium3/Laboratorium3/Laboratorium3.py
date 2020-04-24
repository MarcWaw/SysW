#Autor: Marcin Wawszczak 235274
#Program na Labolatorium 3 Systemów Wbudowanych

import re

text = """From: author@example.com
User-Agent: Thunderbird 1.5.0.9 (X11/20061227)
MIME-Version: 1.0
To: editor@example.com """

temp1 = text.splitlines()    #przechowywanie linii
temp2 = []                   #przechowywanie rozdzielonych wyrazen


for i in range(len(temp1)):
    temp2.append(re.split(r':\s',temp1[i]))   #oddzielenie przedrostkow od danych

slownik = {}                 #deklaracja slownika

for i in range(len(temp2)):
    slownik[temp2[i][0]] = temp2[i][1]     #uzupelnienie slownika

for klucz in slownik:
    print("%s: %s" % (klucz,slownik[klucz]))   #wyswietl tekst za pomoca slownika

#testy poszczegolnych kluczy
print()
print(slownik["To"])
print(slownik["From"])
print(slownik["User-Agent"])


