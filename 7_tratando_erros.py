nome = input('Digite seu nome: ')

try:
    print(f'A primeira letra do seu nome é {nome[0]}')
except:
    print('O nome não pode estar vazio!')
