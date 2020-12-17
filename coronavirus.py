from pipenv.vendor import requests
from bs4 import BeautifulSoup

print('*' * 40)
print('CORONAVIRUS'.center(40, '*'))
print('*' * 40)
print('_' * 40)
pais = input('Pais[em inglẽs]:').strip()
url = f'https://www.worldometers.info/coronavirus/country/{pais}/'
req = requests.get(url)
soap = BeautifulSoup(req.text, 'html.parser')

if len(soap.find_all('div', 'number-table-main')) == 0:
    casos = casos_com_resultado = '0 ou não identificado.'
else:
    casos = soap.find_all('div', 'number-table-main')[0].text.strip()
    casos_com_resultado = soap.find_all('div', 'number-table-main')[1].text.strip()

if len(soap.find_all('span', 'number-table')) == 0:
    condicoes = casos_serios = recuperados = mortes = '0 ou não identificado.'
else:
    condicoes = soap.find_all('span', 'number-table')[0].text.strip()
    casos_serios = soap.find_all('span', 'number-table')[1].text.strip()
    recuperados = soap.find_all('span', 'number-table')[2].text.strip()
    mortes = soap.find_all('span', 'number-table')[3].text.strip()

casos_total = '0 ou não identificado.' if len(soap.find_all('div', 'maincounter-number')) == 0 else \
    soap.find_all('div', 'maincounter-number')[0].text.strip()

print('_' * 40)
print(f'Casos de coronarvirus:{casos_total}.')
print('_' * 40)
print('Casos Ativos')
print(f'Pacientes altamente infectados:{casos}')
print(f'Em condições suave:{condicoes}')
print(f'Em condiçoes séria ou critica:{casos_serios}')
print('_' * 40)
print('Casos Fechados')
print(f'Casos em que tiveram resultado:{casos_com_resultado}')
print(f'Pacientes recuperados:{recuperados}')
print(f'Quantidade de mortes:{mortes}')
print('-' * 40)
