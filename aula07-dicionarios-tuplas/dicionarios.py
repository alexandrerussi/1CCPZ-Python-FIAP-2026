eng2sp = dict()
print(eng2sp)

eng2sp['one'] = 'uno'
print(eng2sp)

eng2sp = {
    'one': 'uno',
    'two': 'dos'
}

print(eng2sp)
print(eng2sp['two'])

print('dos' in eng2sp)

# CONTAGEM DE LETRAS
def count_letters(s):
    d = dict()
    for c in s: # s = "ovo" | c = "v"
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dict_contagem = count_letters("uva")
print(dict_contagem)

personagens = [
    {
        "nome": "Rick",
        "idade": 70,
        "episodios": ["S01E01", "S01E02", "S01E03", "S01E04"]
    },
    {
        "nome": "Morty",
        "idade": 14,
        "episodios": ["S01E01", "S01E02", "S01E03", "S01E04"]
    }
]

for personagem in personagens:
    nome = personagem["nome"]
    idade = personagem["idade"]
    episodios = personagem["episodios"]

    for key, value in personagem.items():
        print(f"{key}: {value}")
