"""Interface de terminal para o sistema de votação."""

from votacao import SistemaDeVotacao


def mostrar_menu() -> None:
    print("\n===== SISTEMA DE VOTAÇÃO =====")
    print("1. Cadastrar candidato")
    print("2. Votar")
    print("3. Exibir resultados")
    print("0. Encerrar")


def executar() -> None:
    sistema = SistemaDeVotacao()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                nome = input("Nome do candidato: ")
                sistema.adicionar_candidato(nome)
                print(f"Candidato '{nome.strip()}' cadastrado com sucesso.")

            elif opcao == "2":
                if not sistema.obter_resultados():
                    print("Cadastre pelo menos um candidato antes de votar.")
                    continue

                nome = input("Em quem deseja votar? ")
                sistema.registrar_voto(nome)
                print("Voto registrado com sucesso.")
                # Atualiza os resultados imediatamente após cada voto.
                print(sistema.exibir_resultados())

            elif opcao == "3":
                print(sistema.exibir_resultados())

            elif opcao == "0":
                print("Votação encerrada. Resultado final:")
                print(sistema.exibir_resultados())
                break

            else:
                print("Opção inválida. Tente novamente.")

        except (ValueError, TypeError) as erro:
            # Erros esperados são apresentados sem interromper a aplicação.
            print(f"Não foi possível concluir a operação: {erro}")


if __name__ == "__main__":
    executar()
