class CalculadoraNotas:

    def media_aritmetica(self, notas):
        return sum(notas) / len(notas)

    def media_ponderada(self, notas, pesos):
        return sum(n * p for n, p in zip(notas, pesos)) / sum(pesos)

    def maior_nota(self, notas):
        return max(notas)

    def menor_nota(self, notas):
        return min(notas)
