# declarando variavel com conteudo de texto
nome = 'digite seu nome aqui'
# declarando variavel com conteudo de texto
sobrenome = 'digite seu sobrenome aqui'
# declarando variavel com conteudo de numero inteiro
idade = 0
# declarando variavel com conteudo de numero decimal
altura = 0.0
# declarando variavel com conteudo de texto
cidade = 'digite sua cidade aqui'
# declarando variavel com conteudo de lista
bebidas = ['digite sua bebida favorita 1 aqui', 'digite sua bebida favorita 2 aqui']
# declarando variavel com conteudo de dicionario
filmes = {
    'comedia': 'digite seu filme aqui',
    'acao': 'digite seu filme aqui'
}
# declarando variavel com conteudo de boleano
mora_no_exterior = False

# utilizando a funcao print para mostrar o valor das variaveis
print(f'''
### RESULTADO ###

Nome: {nome}

Sobrenome: {sobrenome}

Idade: {idade}

Altura: {altura}

Cidade: {cidade}

Bebidas: {bebidas}

Filme de comedia: {filmes['comedia']}

Filme de acao: {filmes['acao']}

Mora no exterior: {mora_no_exterior}

''')
