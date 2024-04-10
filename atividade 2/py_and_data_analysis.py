import pandas as pd


class QuestoesBasicas:
    # Inicializa a lista de números
    def __init__(self):
        self.numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # QUESTÃO 1
    def questao_1(self):
        return [number for number in self.numeros if number % 2 != 0]

    # QUESTÃO 2
    def questao_2(self):
        return [number for number in self.numeros if self.is_prime(number)]

    # Função auxiliar para verificar se um número é primo
    def is_prime(self, number):
        if number <= 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

    # QUESTÃO 3
    def questao_3(self):
        return list(set(self.numeros) ^ set([2, 5, 6, 9, 10]))

    # QUESTÃO 4
    def questao_4(self):
        # Verifica se a lista tem pelo menos dois elementos
        if len(self.numeros) < 2:
            return "A lista precisa ter pelo menos dois elementos."
        maior = max(self.numeros)

        # Inicializa o segundo maior valor como negativo infinito
        segundo_maior = float('-inf')

        for numero in self.numeros:
            # Atualiza o segundo maior valor se encontrarmos um valor menor do
            # que o maior e maior do que o segundo maior
            if numero != maior and numero > segundo_maior:
                segundo_maior = numero

        # Verifica se encontramos um segundo maior valor válido
        if segundo_maior == float('-inf'):
            return "Não há segundo maior valor na lista."

        return segundo_maior

    # QUESTÃO 5
    def questao_5(self):
        return sorted([("João", 20), ("Maria", 30), ("Ana", 25), ("Pedro", 27)])


class VisualizacaoDados:
    def questao_6(self):
        import matplotlib.pyplot as plt
        import numpy as np

        fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), 
                                constrained_layout=True)

        for row in range(2):
            for col in range(2):
                axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                                       transform=axs[row, col].transAxes,
                                       ha='center', va='center', fontsize=18,
                                       color='darkgrey')

        fig.suptitle('plt.subplots()')
        plt.show()

    def questao_7(self):
        import numpy as np
        import matplotlib as mpl
        import matplotlib.pyplot as plt

        x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
        y = np.sin(x)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        plt.show()

    def questao_8(self):
        df = pd.read_csv('arquivo.csv')
        print(df.head())

    def questao_9(self):
        df = pd.read_csv('arquivo.csv')
        coluna = df['coluna']
        filtro = df['coluna'] > 10
        print(df[filtro])

    def questao_10(self):
        df = pd.read_csv('arquivo.csv')
        df.fillna(0, inplace=True)
        print(df)


# Teste das questões
questoes_basicas = QuestoesBasicas()
visualizacao_dados = VisualizacaoDados()

print("Questões Básicas:")
print(questoes_basicas.questao_1())
print(questoes_basicas.questao_2())
print(questoes_basicas.questao_3())
print(questoes_basicas.questao_4())
print(questoes_basicas.questao_5())

print("\nVisualização de Dados:")
visualizacao_dados.questao_6()
visualizacao_dados.questao_7()

# Não é possível testar as questões 8, 9 e 10 sem o arquivo csv
