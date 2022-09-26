from main import somar, subtrair, dividir, multiplicar


class teste_calculos:
    def teste_somar(self):
        # 1 - Configura
        numero_a = 8
        numero_b = 7
        resultado_esperado = 15

        # 2 Executa
        resultado_obtido = somar(numero_a, numero_b)

        # 3 Valida
        assert(resultado_obtido==resultado_esperado)


    def teste_subtrair(self):
        # 1 - Configura
        numero_a = 8
        numero_b = 7
        resultado_esperado = 1

        # 2 - Executa
        resultado_obtido = subtrair(numero_a, numero_b)

        # 3 - Valida
        assert(resultado_obtido == resultado_esperado)


    def teste_dividir(self):
            # 1 - Configura
            numero_a = 8
            numero_b = 2
            resultado_esperado = 4

            # 2 - Executa
            resultado_obtido = dividir(numero_a, numero_b)

            # 3 - Valida
            assert (resultado_obtido == resultado_esperado)


    def teste_dividir_por_zero(self):
            # 1 - Configura
            numero_a = 8
            numero_b = 0
            resultado_esperado = 'Não dividirás por zero'

            # 2 - Executa
            resultado_obtido = dividir(numero_a, numero_b)

            # 3 - Valida
            assert (resultado_obtido == resultado_esperado)


    def teste_multiplicar(self):
            # 1 - Configura
            # 1.1 Dados de entrada
            numero_a = 8
            numero_b = 4
            # 1.2 Resultado esperado
            resultado_esperado = 32

            # 2 - Executa
            resultado_obtido = multiplicar(numero_a, numero_b)

            # 3 - Valida
            assert (resultado_obtido == resultado_esperado)
