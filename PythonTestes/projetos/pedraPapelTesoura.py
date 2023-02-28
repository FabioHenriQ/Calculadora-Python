from random import choice

jogador_vitorias = 0
maq_vitorias = 0


def opcao_jogador():
    esc_jogador = input("Escolha pedra, papel ou tesoura ")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    else:
        print("Opcao invalida. Tente novamente")
        opcao_jogador()


def opcao_maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina


while True:

    print("-"*60)
    esc_jogador = opcao_jogador()
    esc_maquina = opcao_maquina()
    print("-"*60)

    if (esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra") \
            or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
        print(f"""Voce escolheu: {esc_jogador}
            e ele: {esc_maquina}""")
        print("Voce ganhou")
        jogador_vitorias += 1

    elif esc_jogador == esc_maquina:
        print("Deu empate")

    else:
        print(f"""Voce escolheu: {esc_jogador}
            e ele: {esc_maquina}""")
        print("Voce perdeu")
        maq_vitorias += 1

    print("-"*60)
    print(f"Vitorias do jogador: {jogador_vitorias}")
    print(f"Vitorias do maquina: {maq_vitorias}")
    print("-"*60)

    esc_jogador = input("Quer jogar novamente? (Sim | nao): ")
    if esc_jogador in ["sim", "Sim", "ss", "SS", "s", "S"]:
        pass
    elif esc_jogador in ["Nao", "nao", "nn", "NN", "n", "N"]:
        break
    else:
        break
