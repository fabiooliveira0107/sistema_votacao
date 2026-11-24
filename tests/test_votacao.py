"""Testes automatizados do núcleo do sistema."""

import unittest

from votacao import Candidato, SistemaDeVotacao


class TestCandidato(unittest.TestCase):
    def test_candidato_recebe_voto(self):
        candidato = Candidato("Ana")
        candidato.receber_voto()
        self.assertEqual(candidato.votos, 1)

    def test_nome_vazio_nao_e_permitido(self):
        with self.assertRaises(ValueError):
            Candidato("   ")


class TestSistemaDeVotacao(unittest.TestCase):
    def setUp(self):
        self.sistema = SistemaDeVotacao()
        self.sistema.adicionar_candidato("Ana")
        self.sistema.adicionar_candidato("Bruno")

    def test_registrar_voto(self):
        self.sistema.registrar_voto("Ana")
        self.assertEqual(self.sistema.total_de_votos(), 1)
        self.assertEqual(self.sistema.obter_resultados()[0], ("Ana", 1))

    def test_candidato_inexistente(self):
        with self.assertRaises(ValueError):
            self.sistema.registrar_voto("Carla")

    def test_nao_permite_candidato_duplicado_ignorando_caixa(self):
        with self.assertRaises(ValueError):
            self.sistema.adicionar_candidato("ANA")

    def test_resultados_ordenados_por_votos(self):
        self.sistema.registrar_voto("Bruno")
        self.sistema.registrar_voto("Bruno")
        self.sistema.registrar_voto("Ana")
        self.assertEqual(
            self.sistema.obter_resultados(),
            [("Bruno", 2), ("Ana", 1)]
        )

    def test_exibicao_sem_votos(self):
        texto = self.sistema.exibir_resultados()
        self.assertIn("Total de votos: 0", texto)


if __name__ == "__main__":
    unittest.main()
