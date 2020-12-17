from pipenv.vendor.requests import post

num = int(input('Gerar quantos CPFs??'))
listacpf = []
for repetir in range(0, num):
    requisicao = post('https://www.4devs.com.br/ferramentas_online.php', {'acao': 'gerar_cpf', 'pontuacao': 'S', 'estado': ''})

    resposta = requisicao.text
    cpf = resposta[0:14]
    print(cpf)

    listacpf.append(resposta[0:14])
    cpf = open('ListaDeCpf.txt', 'w', encoding='utf-8')
    for i in listacpf:
        cpf.write(str("'"+i+"'"'#'))
