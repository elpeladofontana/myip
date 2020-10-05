from requests import get

ip = get('https://api.ipify.org').text
print ('mi ip en internet es: ', ip)
