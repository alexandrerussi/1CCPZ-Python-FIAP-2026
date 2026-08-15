endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

# FUNÇÃO que verifica se UM código HTTP de uma req
# é sucesso ou não
# 200 -> True
# 401 -> False
def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

# FUNÇÃO que verifica se tem 2 erros seguidos na
# lista de requisições (codigos http) de UM endpoint
# [200, 200, 401, 200, 500] -> False
# [201, 500, 502, 201, 500] -> True
def verifica_erros(codigos_endpoint):
    for i in range(len(codigos_endpoint) - 1):
        codigo_atual = codigos_endpoint[i]
        prox_codigo = codigos_endpoint[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

print(verifica_erros(status[0]))