base_emails = """
teste8472@alura.com.br, contato391@fiap.com.br, aluno5821@alun.com.br, usuario174@alura.com.br, dev9283@fiap.com.br, estudante461@alun.com.br, projeto735@alura.com.br, curso1846@fiap.com.br, aluno9027@alun.com.br, teste316@alura.com.br, contato7642@fiap.com.br, usuario5389@alun.com.br, dev271@alura.com.br, estudante843@fiap.com.br, projeto6157@alun.com.br, aluno492@alura.com.br, teste7284@fiap.com.br, usuario3619@alun.com.br, curso527@alura.com.br, dev9163@fiap.com.br, contato2841@alun.com.br, estudante673@alura.com.br, aluno8052@fiap.com.br, projeto4397@alun.com.br, teste152@alura.com.br, usuario6849@fiap.com.br, dev3175@alun.com.br, curso926@alura.com.br, contato5413@fiap.com.br, aluno7826@alun.com.br, estudante394@alura.com.br, projeto8617@fiap.com.br, teste5294@alun.com.br, usuario746@alura.com.br, dev2381@fiap.com.br, contato9057@alun.com.br, aluno614@alura.com.br, curso4728@fiap.com.br, estudante3516@alun.com.br, projeto827@alura.com.br, teste6931@fiap.com.br, usuario4185@alun.com.br, dev752@alura.com.br, contato3269@fiap.com.br, aluno5847@alun.com.br, estudante913@alura.com.br, projeto6472@fiap.com.br, teste2856@alun.com.br, usuario7394@alura.com.br, curso168@fiap.com.br, dev5247@alun.com.br, contato816@alura.com.br, aluno3972@fiap.com.br, estudante6541@alun.com.br, projeto283@alura.com.br, teste9476@fiap.com.br, usuario5318@alun.com.br, curso729@alura.com.br, dev4613@fiap.com.br, contato8752@alun.com.br, aluno246@alura.com.br, estudante7185@fiap.com.br, projeto9364@alun.com.br, teste384@alura.com.br, usuario6297@fiap.com.br, dev1538@alun.com.br, contato472@alura.com.br, curso8451@fiap.com.br, aluno6935@alun.com.br, estudante217@alura.com.br, projeto5769@fiap.com.br, teste8314@alun.com.br, usuario465@alura.com.br, dev7926@fiap.com.br, contato3187@alun.com.br, aluno954@alura.com.br, curso6213@fiap.com.br, estudante5482@alun.com.br, projeto176@alura.com.br, teste7635@fiap.com.br, usuario2948@alun.com.br, dev587@alura.com.br, contato9361@fiap.com.br, aluno4725@alun.com.br, estudante819@alura.com.br, projeto3546@fiap.com.br, teste6812@alun.com.br, usuario927@alura.com.br, curso5138@fiap.com.br, dev2469@alun.com.br, contato758@alura.com.br, aluno8347@fiap.com.br, estudante1625@alun.com.br, projeto497@alura.com.br, teste5726@fiap.com.br, usuario3814@alun.com.br, dev649@alura.com.br
"""

# Quebrar a string em uma lista (array)
emails_lista = [email.strip() for email in base_emails.split(",")]

# Dicionário para contar qtos e-mails por dominio
dominios_count = {}
dominios_users = {}

# Lista para armazenar nomes de usuario
usuarios = []

# Processar cada e-mail
for email in emails_lista:
    # Separar nome de usuario e dominio
    usuario, dominio = email.split("@")
    usuarios.append(usuario)

    # contar dominios
    if dominio not in dominios_count:
        dominios_count[dominio] = 1
        dominios_users[dominio] = [usuario]
    else:
        dominios_count[dominio] += 1
        dominios_users[dominio].append(usuario)

print(dominios_count)
print(dominios_users)

# converter a lista de usuarios para tupla
usuarios_tupla = tuple(usuarios)

# trocar primeiro e ultimo usuario usando tuplas
usuarios_tupla_invertido = list(usuarios_tupla)
usuarios_tupla_invertido[0], usuarios_tupla_invertido[-1] = usuarios_tupla_invertido[-1], usuarios_tupla_invertido[0]
usuarios_tupla_invertido = tuple(usuarios_tupla_invertido)

# print(usuarios_tupla)
# print(usuarios_tupla_invertido)

# exibir relatorio final

print("\nRelatório")
print("Qtd de e-mails por dominio:")
for dominio, qtd in dominios_count.items():
    print(f"{dominio}: {qtd}")

