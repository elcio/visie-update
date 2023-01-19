import requests

faixas = requests.get('https://update.visie.com.br/faixas.json').json()

for faixa in faixas:
    print('=' * 60)
    for k, v in faixa.items():
        print(f'{k.upper()}:')
        print(f'  {v}')
