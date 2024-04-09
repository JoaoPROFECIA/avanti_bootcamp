# Python and data analysis

# Algoritmos básicos de programação em linguagem python e
# visualização e análise de dados

# Numeros utilizados para as questões são predefinidos e armazenados na
# variável numeros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# QUESTÃO 1
# Função para retornar números ímpares de uma lista de números

def odd_numbers(numbers):
    return [number for number in numbers if number % 2 != 0]


# Chamando a função odd_numbers para obter o resultado
resultado_odd_numbers = odd_numbers(numeros)

questions_and_answers_1 = {
    "1. Escreva uma função que receba uma lista de números e retorne outra"
    "lista com os números ímpares.":
        "def odd_numbers(numbers):\n"
        "    return [number for number in numbers if number % 2 != 0]"
}


# QUESTÃO 2
# Função para retornar números únicos de uma lista de números

def unique_numbers(numbers):
    return list(set(numbers))


questions_and_answers_2 = {
    "2. Escreva uma função que receba uma lista de números e retorne outra "
    "lista com números presentes.":
        "def unique_numbers(numbers):\n"
        "    return list(set(numbers))",
}
resposta_2 = {
    "resposta_2": {
        "unique_numbers_function": unique_numbers(numeros)
    }
}


# QUESTÃO 3
# Função para retornar elementos presentes em apenas uma das listas

def elements_in_one_list_only(list1, list2):
    return list(set(list1) ^ set(list2))


questions_and_answers_3 = {
    "3. Escreva uma função que receba duas listas e retorne outra lista com os"
    "elementos presentes em apenas uma das listas.":
        "def elements_in_one_list_only(list1, list2):\n"
        "    return list(set(list1) ^ set(list2))",
}

resultado_elements_in_one_list_only = elements_in_one_list_only(
    numeros, [2, 4, 6, 8, 10]
    )

resposta_3 = {
    "resposta_3": {
        "elements_in_one_list_only_function":
            resultado_elements_in_one_list_only
    }
}


# QUESTÃO 4
# Função para retornar o segundo maior valor de uma lista de números

def segundo_maior_valor(lista_de_numeros):
    lista_ordenada = sorted(lista_de_numeros, reverse=True)
    return lista_ordenada[1]


questions_and_answers_4 = {
    "4. Dada uma lista de números inteiros, escreva uma função para encontrar"
    "o segundo maior valor na lista.":
        "def segundo_maior_valor(lista_de_numeros):\n"
        "    lista_ordenada = sorted(lista_de_numeros, reverse=True)\n"
        "    return lista_ordenada[1]",
}
resposta_4 = {
    "resposta_4": {
        "segundo_maior_valor_function": segundo_maior_valor(numeros)
    }
}


# QUESTÃO 5
# Função para ordenar uma lista de tuplas pelo nome das pessoas

def ordenar_por_nome(lista_de_pessoas):
    return sorted(lista_de_pessoas, key=lambda pessoa: pessoa[0])


questions_and_answers_5 = {
    "5. Crie uma função que receba uma lista de tuplas, cada uma contendo o"
    "nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das"
    "pessoas em ordem alfabética.":
        "def ordenar_por_nome(lista_de_pessoas):\n"
        "    return sorted(lista_de_pessoas, key=lambda pessoa: pessoa[0])",
}
resposta_5 = {
    "resposta_5": {
        "ordenar_por_nome_function": ordenar_por_nome(
            [("João", 20), ("Maria", 30), ("Ana", 25)]
            )
    }
}


# Função para exibir perguntas e respostas

def display_questions_and_answers():
    print("Numeros utilizados:", numeros)
    print()
    for question, answer in questions_and_answers_1.items():
        print(question)
        print(answer)
        print("Resposta 1:",
              resultado_odd_numbers
              )
        print()

    for question, answer in questions_and_answers_2.items():
        print(question)
        print(answer)
        print("Resposta 2:",
              resposta_2
              ["resposta_2"]
              ["unique_numbers_function"]
              )
        print()

    for question, answer in questions_and_answers_3.items():
        print(question)
        print(answer)
        print("Resposta 3:",
              resposta_3
              ["resposta_3"]
              ["elements_in_one_list_only_function"]
              )
        print()

    for question, answer in questions_and_answers_4.items():
        print(question)
        print(answer)
        print("Resposta 4:",
              resposta_4
              ["resposta_4"]
              ["segundo_maior_valor_function"]
              )
        print()

    for question, answer in questions_and_answers_5.items():
        print(question)
        print(answer)
        print("Resposta 5:",
              resposta_5
              ["resposta_5"]
              ["ordenar_por_nome_function"]
              )
        print()


# Chamada da função para exibir perguntas e respostas

display_questions_and_answers()
