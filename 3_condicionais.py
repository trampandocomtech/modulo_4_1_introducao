a = 2
b = 2
tipo = 'SOMA'

# comando para verificar se a variavel tipo possui o valor igual a SOMA, se essa condicao
# for verdadeira executará o comando que está dentro desse bloco
if tipo == 'SOMA':
    # somando o valor de a com b
    c = a + b

# comando para verificar se a variavel tipo possui o valor igual a SUBTRACAO, se essa condicao
# for verdadeira executará o comando que está dentro desse bloco
if tipo == 'SUBTRACAO':
    # subtraindo o valor de a com b
    c = a - b

# comando para verificar se a variavel tipo possui o valor igual a MULTIPLICACAO, se essa condicao
# for verdadeira executará o comando que está dentro desse bloco
if tipo == 'MULTIPLICACAO':
    # multiplicando o valor de a com b
    c = a * b

# comando para verificar se a variavel tipo possui o valor igual a DIVISAO, se essa condicao
# for verdadeira executará o comando que está dentro desse bloco
if tipo == 'DIVISAO':
    # divindo o valor de a com b
    c = a / b

# comando para verificar se a variavel tipo possui o valor igual a RESTO, se essa condicao
# for verdadeira executará o comando que está dentro desse bloco
if tipo == 'RESTO':
    # resto da divisão de a com b
    c = a % b


print(f'RESULTADO DA {tipo}')
print(c)
