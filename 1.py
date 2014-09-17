#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
f = open('readwrite.txt', 'r+')
f1 = open('inputdata.txt','r+')
a=int(f1.readline())
print (a)
b=a*a
print (b)

a1=1
while a1 < a:
	asq = a1 * a1 * 1.0
	s=str(a1)
	s2=str(asq)
	s3 = s+" "+s2+"\n"
	a1=a1+1
	f.write(s3)

f.close()
f1.close()	

import sys
print(sys.version)
