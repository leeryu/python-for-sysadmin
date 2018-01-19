import requests

res = requests.get('http://localhost:9999/echo/Mother')

if res.status_code == 200 and \
    res.text == 'Say hello to my little friend: Mother!':
    print('It worked! That almost never happens!')  
else:
    print('Argh, got this:', res.text)