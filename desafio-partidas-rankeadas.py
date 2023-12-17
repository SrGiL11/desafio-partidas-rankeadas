def calcular_nivel(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas
    nivel = ""

    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return f"O Herói tem um saldo de {saldo_vitorias} está no nível de {nivel}"

# Exemplo de uso da função
resultado = calcular_nivel(75, 25)
print(resultado)