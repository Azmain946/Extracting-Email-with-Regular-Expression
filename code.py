import re
import requests
import csv

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
res=requests.get('https://en.wikipedia.org/wiki/Email_address#:~:text=The%20general%20format%20of%20an,the%20recipient%2C%20e.g.%2C%20jsmith.').text

#print(res)
r=re.compile(r'([.\w]+@\w+[.]\w+)',re.M)
li=r.findall(res)

with open('Email.csv','w',newline='',encoding='utf-8') as f:
		writer=csv.DictWriter(f,["Email"])
		for i in li:
				writer.writerow({"Email":i})
