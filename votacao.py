"""
Núcleo do sistema de votação.

Contém as classes Candidato e SistemaDeVotacao. A camada de domínio não
depende da interface de terminal, facilitando testes e reutilização.
"""

from dataclasses import dataclass


@dataclass
class Candidato:
    """Representa um candidato e mantém sua quantidade de votos."""

    nome: str
    votos: int = 0

    def __post_init__(self) -> None:
        self.nome = self.nome.strip()
        if not self.nome:
            raise ValueError("O nome do candidato não pode ficar vazio.")
        if self.votos < 0:
            raise ValueError("A quantidade de votos não pode ser negativa.")

    def receber_voto(self) -> None:
        """Registra um voto para este candidato."""
        self.votos += 1


class SistemaDeVotacao:
    """Gerencia candidatos, registro de votos e consulta de resultados."""

    def __init__(self) -> None:
        # Dicionário indexado pelo nome normalizado para localizar candidatos.
        self._candidatos: dict[str, Candidato] = {}

    @staticmethod
    def _normalizar_nome(nome: str) -> str:
        """Padroniza espaços e caixa para evitar cadastros duplicados."""
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser um texto.")
        nome = " ".join(nome.strip().split())
        if not nome:
            raise ValueError("O nome não pode ficar vazio.")
        return nome.casefold()

    def adicionar_candidato(self, nome: str) -> Candidato:
        """Adiciona um candidato; nomes repetidos não são permitidos."""
        chave = self._normalizar_nome(nome)
        if chave in self._candidatos:
            raise ValueError(f"O candidato '{nome}' já está cadastrado.")

        candidato = Candidato(nome=nome)
        self._candidatos[chave] = candidato
        return candidato

    def registrar_voto(self, nome_candidato: str) -> None:
        """Registra um voto ou informa se o candidato não existe."""
        chave = self._normalizar_nome(nome_candidato)
        candidato = self._candidatos.get(chave)
        if candidato is None:
            raise ValueError(
                f"O candidato '{nome_candidato}' não está registrado."
            )
        candidato.receber_voto()

    def obter_resultados(self) -> list[tuple[str, int]]:
        """
        Retorna os resultados ordenados por votos (maior primeiro).
        Em caso de empate, ordena alfabeticamente pelo nome.
        """
        resultados = [
            (candidato.nome, candidato.votos)
            for candidato in self._candidatos.values()
        ]
        return sorted(resultados, key=lambda item: (-item[1], item[0].casefold()))

    def total_de_votos(self) -> int:
        """Retorna o total de votos registrados."""
        return sum(candidato.votos for candidato in self._candidatos.values())

    def exibir_resultados(self) -> str:
        """Monta uma representação textual dos resultados atuais."""
        resultados = self.obter_resultados()
        if not resultados:
            return "Ainda não há candidatos cadastrados."

        total = self.total_de_votos()
        linhas = ["\n=== RESULTADOS ATUAIS ==="]
        for nome, votos in resultados:
            percentual = (votos / total * 100) if total else 0
            linhas.append(f"{nome}: {votos} voto(s) ({percentual:.1f}%)")
        linhas.append(f"Total de votos: {total}")
        return "\n".join(linhas)
