nome = input('Digite seu nome: ')

if nome[0].isdigit():
    raise Exception('O nome não pode ser um número!')

print(f'A primeira letra do seu nome é {nome[0]}')
