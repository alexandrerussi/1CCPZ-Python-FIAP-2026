# imagina.. um sistema que recolha a escolha do usuário
# escolha_usuário
# se...
# 0 --> sair do programa
# 1 --> entrar no programa
# ----> erro!

escolha_usuario = 13214

match escolha_usuario:
    case 0:
        print("sair do programa")
    case 1:
        print("entrar no programa")
    case _:
        print("Erro!!")
