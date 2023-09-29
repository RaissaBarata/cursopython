# operadores ternários: expressão + condição verdadeira ou condição falsa

idade = 20
status = "maior de idade" if idade >= 18 else "menor de idade"
print(status)

# operador de membro: é usado para verificar se um determinado valor está presente em uma sequencia (lista, conjunto, etc). Para isso usamos IN ou NOT IN.

frutas = ["maca", "banana", "laranja"]
existe_maca = "maca" in frutas  # retorna true
existe_uva = "uva" in frutas  # retorna false pois não esta na lista
print(existe_uva)

lista = [1, 2, 3, "Ana", "Carla"]
existe = "Ana" not in lista
print(existe)

# operador de identidade: são utilizados para comparar a identidade de objetos, ou seja, verifica se duas variáveis estão fazendo referência ao mesmo objeto na memória. (is: retorna true se duas variáveis estiverem se referindo ao mesmo tempo e false se o contrário; is not: retorna true se duas variáveis não estiverem se referindo ao mesmo objeto e false caso contrário).abs

x = 3
y = x
z = 3

print(x is z)
print(y is z)
print(x is not z)

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # retorna true, a e b estão se referindo ao mesmo objeto
print(
    a is c
)  # retorna false, pois embora tenham o mesmo conteúdo são listas diferentes.
print(b is not c)
