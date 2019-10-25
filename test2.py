import requests

#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://https://www.eprover.com/main.html')

#print the response text (the content of the requested file):
print(x.text)
