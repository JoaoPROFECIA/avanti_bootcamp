# Questões e respostas

questions_and_answers = {
    "1. O que é Machine Learning?":
        "1.1. É uma técnica de Inteligência Artificial (IA) que permite que um"
        " sistema aprenda a partir de dados.",
    "2. Explique o conceito de conjunto de treinamento, conjunto de validação"
    " e conjunto de teste em Machine Learning.":
        "2.1. Conjunto de treinamento: é o conjunto de dados que é utilizado"
        " para treinar o modelo de Machine Learning.\n"
        "2.2. Conjunto de validação: é o conjunto de dados que é utilizado "
        "para ajustar os hiperparâmetros do modelo de Machine Learning.\n"
        "2.3. Conjunto de teste: é o conjunto de dados que é utilizado para "
        "avaliar o desempenho do modelo de Machine Learning.",
    "3. Explique como você lidaria com dados ausentes em um conjunto de dados"
    " de treinamento.":
        "3.1. Uma das formas de lidar com dados ausentes em um conjunto de "
        "dados de treinamento é preencher os valores ausentes com a média dos "
        "valores existentes.",
    "4. O que é uma matriz de confusão e como ela é usada para avaliar o "
    "desempenho de um modelo preditivo?":
        "4.1. A matriz de confusão é uma "
        "tabela que é utilizada para avaliar desempenho de um modelo "
        "preditivo. Ela é composta por quatro células: Verdadeiro Positivo "
        "(VP), Falso Positivo (FP), Verdadeiro Negativo (VN) e Falso Negativo "
        "(FN).\n"
        "4.2. A matriz de confusão é utilizada para calcular métricas como a "
        "acurácia, a precisão, a sensibilidade e a especificidade do modelo "
        "preditivo.\n"
        "4.2.1. A acurácia é a proporção de predições corretas feitas pelo "
        "modelo.\n"
        "4.2.2. A precisão é a proporção de predições corretas feitas pelo "
        "modelo entre todas as predições positivas feitas pelo modelo.\n"
        "4.2.3. A sensibilidade é a proporção de predições corretas feitas "
        "pelo modelo entre todos os exemplos positivos existentes no conjunto "
        "de dados.\n"
        "4.2.4. A especificidade é a proporção de predições corretas feitas "
        "pelo modelo entre todos os exemplos negativos existentes no conjunto "
        "de dados.\n"
        "A matriz de confusão é uma ferramenta importante para avaliar o "
        "desempenho de um modelo preditivo, pois permite identificar os erros "
        "cometidos pelo modelo e ajustar o modelo para melhorar o seu "
        "desempenho.",
    "5. Em quais áreas (tais como construção civil, agricultura, saúde, "
    "manufatura, entre outras) você acha mais interessante aplicar algoritmos "
    "de machine learning":
        "5.1. A área onde é interessante aplicar (ou aprimorar) algoritmos de "
        "Machine Learning é a área governamental, pois permite que os "
        "representantes políticos assumam decisões eficientes com base em "
        "dados e análises, assim, provendo a eficácia dos serviços prestados e"
        ", consequentemente, melhorando a qualidade de vida dos cidadãos."
}

# Função para exibir perguntas e respostas


def display_questions_and_answers():
    for question, answer in questions_and_answers.items():
        print(question)
        print(answer)
        print()

# Chamada da função para exibir perguntas e respostas


display_questions_and_answers()

