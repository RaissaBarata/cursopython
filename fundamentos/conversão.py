# conversão de tipos:

a = 2  # numero inteiro
b = "3"  # string
c = 3.5

print(type(a))  # retornará class int
print(type(b))  # retornará class str
print(type(c))  # retornará class float

# para converter:
print(a + int(b))  # converto a var b em inteira para somar
print(str(a) + b)  # converto a var a em string para concatenar
print(2 + float(c))  # para calcular numeros de ponto flutuante com numeros inteiros

# coerção automática: refere-se a capacidade da linguagem de converter automaticamente tipos de dados para outro quando necessário para realizar operações ou avaliar expressões. isso ocorre principalmente em operações envolvendo diferentes tipos de dados.

x = 5
y = 2.5
print(x + y)

divisao = 10 / 2
print(type(divisao))  # o resultado é tipo float

# se eu quiser que a operação gere um tipo inteiro:
divisao_inteiro = 10 // 3
print(divisao_inteiro)  # o resultado será 3


texto = "o numero e: "  # o texto é uma string
numero = 42  # numero int

# neste caso, a coerção automatica de tipos não ocorre nesse caso, pois a concatenação de uma string com um numero inteiro não é válido em python, portanto, deve-se fazer:

print(texto + str(numero))
