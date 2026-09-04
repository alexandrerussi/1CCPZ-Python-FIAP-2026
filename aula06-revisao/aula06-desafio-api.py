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

# LISTA DE REQUISIÇÕES DE 1 ENDPOINT
# [200, 200, 401, 200, 500]
# [201, 500, 502, 201, 500]
def analisar_endpoint(codigos_endpoint):
    qtd_sucessos = 0

    for codigo in codigos_endpoint:
        if eh_sucesso(codigo):
            qtd_sucessos += 1

    qtd_total = len(codigos_endpoint)
    qtd_erros = qtd_total -qtd_sucessos
    percentual_sucesso = (qtd_sucessos / qtd_total) * 100

    tem_erros_seguidos = verifica_erros(codigos_endpoint)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif percentual_sucesso >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return (qtd_sucessos, qtd_erros, percentual_sucesso, classificacao)

# PERCORRER A MATRIZ status

maior_erro = 0
endpoint_maior_erro = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    codigos_http = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(codigos_http)

    if erros > maior_erro:
        maior_erro = erros
        endpoint_maior_erro = nome_endpoint

    print(f"Endpoint: {nome_endpoint}")
    print(f"Requisições: {codigos_http}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"% de sucessos: {percentual}")
    print(f"Classificação: {classificacao}")
    print("-" * 30)
    print()

print(f"Endpoint maior erro: {endpoint_maior_erro} ({maior_erro})")
