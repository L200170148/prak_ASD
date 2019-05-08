#no 1
import re

f=open('indonesia.txt', 'r', encoding='latin1')
teks= f.read()
f.close()

pola= r'me\w+'

tampilan=re.findall(pola,teks)
print(tampilan)

print('\n\n')
#no 2
import re

f=open('indonesia.txt', 'r', encoding='latin1')
teks= f.read()
f.close()

pola1= r'di\w+'

tampilan1=re.findall(pola1,teks)
print(tampilan1)

print('\n\n')
#no 3
import re

f=open('indonesia.txt', 'r', encoding='latin1')
teks= f.read()
f.close()

pola2= r'di \w+'

tampilan2=re.findall(pola2,teks)
print(tampilan2)

print('\n\n')
#NO 4
import re
f = open('KEI.htm', 'r', encoding='latin1')

teks = f.read()

strings = re.findall(r'title="([\w+]+)">', teks)
strings= re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>', teks)
a = []
for i in strings:
    a.append((i[0], float(i[1])))

print(a)
