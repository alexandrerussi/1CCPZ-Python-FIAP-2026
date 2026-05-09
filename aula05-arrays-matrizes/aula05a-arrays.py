lista_frutas = ["Banana", "Maçã", "Morango"]

# lista_frutas[0] = "Banana"
# lista_frutas[1] = "Maçã"
# lista_frutas[2] = "Morango"
print(lista_frutas[1])

lista_frutas.append("Uva")
print(lista_frutas[-1])

tamanho = len(lista_frutas)
print(tamanho)
print()

for i in range(tamanho):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)

msg = "Oi fulano!"

for i in range(len(msg)):
    print(msg[i])