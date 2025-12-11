import unittest
from calculadora_notas import CalculadoraNotas

class TestCalculadoraNotas(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraNotas()
        self.notas = [7.0, 8.0, 9.0]
        self.pesos = [2, 3, 5]

    def test_media_aritmetica(self):
        self.assertEqual(self.calc.media_aritmetica(self.notas), 8.0)

    def test_media_ponderada(self):
        self.assertAlmostEqual(
            self.calc.media_ponderada(self.notas, self.pesos), 8.3
        )

    def test_maior_nota(self):
        self.assertEqual(self.calc.maior_nota(self.notas), 9.0)

    def test_menor_nota(self):
        self.assertEqual(self.calc.menor_nota(self.notas), 7.0)

if __name__ == "__main__":
    unittest.main()
