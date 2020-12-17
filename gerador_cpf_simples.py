from pipenv.vendor.requests import post

num = int(input('Digite a Quantidade de CPF >>>'))
for repetir in range(0, num):
    request = post('https://www.4devs.com.br/ferramentas_online.php', {"acao": "gerar_cpf", "pontuacao": "S", "cpf_estado": "sp"})
    resp = request.text
    cpf = resp[0:14]
    print(cpf)
