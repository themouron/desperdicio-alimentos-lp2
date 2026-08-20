import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from src.dados import ALIMENTOS, adicionar_registro, carregar_historico
from src.desperdicio import calcular_desperdicio, classificar_desperdicio
from src.planejamento import estimar_consumo


class ClassificacaoTest(unittest.TestCase):
    def test_limites_das_classificacoes(self):
        casos = [(5, "Excelente"), (10, "Bom"), (15, "Atenção"), (15.1, "Crítico")]
        for percentual, esperado in casos:
            with self.subTest(percentual=percentual):
                self.assertEqual(classificar_desperdicio(percentual), esperado)

    def test_calculo_do_desperdicio(self):
        resultado = calcular_desperdicio(10, 2, 7.5)
        self.assertEqual(resultado["Quantidade consumida"], 8)
        self.assertEqual(resultado["Percentual de desperdício"], 20)
        self.assertEqual(resultado["Valor total comprado"], 75)
        self.assertEqual(resultado["Valor desperdiçado"], 15)
        self.assertEqual(resultado["Classificação"], "Crítico")


class PlanejamentoTest(unittest.TestCase):
    def test_estimativa_em_quilos(self):
        item = ALIMENTOS["Proteínas"][0]
        self.assertEqual(estimar_consumo(item, 10), (1300, 1.3, "kg"))

    def test_estimativa_em_litros(self):
        item = ALIMENTOS["Bebidas"][0]
        self.assertEqual(estimar_consumo(item, 5), (1000, 1, "litros"))


class PersistenciaTest(unittest.TestCase):
    def test_salvar_e_carregar_historico(self):
        with TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "historico.json"
            historico = []
            registro = {"Alimento": "Arroz", "Valor desperdiçado": 2.5}

            adicionar_registro(registro, historico, caminho)

            self.assertEqual(carregar_historico(caminho), [registro])

    def test_arquivo_inexistente_retorna_lista_vazia(self):
        with TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "inexistente.json"
            self.assertEqual(carregar_historico(caminho), [])


if __name__ == "__main__":
    unittest.main()
