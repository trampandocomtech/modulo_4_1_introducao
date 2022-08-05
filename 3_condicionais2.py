a = 2
b = 2
tipo = 'SOMA'

# comando para verificar se a variavel tipo possui o valor igual a SOMA, se essa condicao
# for verdadeira executará o comando que está dentro desse bloco
# se alguma das condicoes forem atendidas será executado o comando dentro do bloco, se nao o bloco
# com a condicional else será executada
if tipo == 'SOMA':
    # somando o valor de a com b
    c = a + b
elif tipo == 'SUBTRACAO':
    # subtraindo o valor de a com b
    c = a - b
elif tipo == 'MULTIPLICACAO':
    # multiplicando o valor de a com b
    c = a * b
elif tipo == 'DIVISAO':
    # divindo o valor de a com b
    c = a / b
else:
    # resto da divisão de a com b
    c = a % b


print(f'RESULTADO DA {tipo}')
print(c)
