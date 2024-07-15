"""
Construa um algoritmo de busca contendo um vetor de números
inteiros de 20 posições.

    • O algoritmo deve ter duas funções, uma para busca sequencial e
        outra para busca binária.
    • Coloque um contador em cada função para contar as iterações de
        cada função.
    • Peça ao usuário que informe o valor que deseja procurar.
    • Então informe ao usuário se este valor existe no vetor e quantas
        iterações foram necessárias em cada função.
"""

import random

# Generate a vector of 20 random integers
vector = [random.randint(1, 100) for _ in range(20)]
vector.sort()  # Sorting the vector for binary search


def sequential_search(vector, target):
    iterations = 0
    for i in range(len(vector)):
        iterations += 1
        if vector[i] == target:
            return True, iterations
    return False, iterations


def binary_search(vector, target):
    left, right = 0, len(vector) - 1
    iterations = 0
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if vector[mid] == target:
            return True, iterations
        elif vector[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False, iterations


def get_user_input():
    while True:
        try:
            user_input = int(input("Enter the value you want to search for: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter an integer value.")


# Ask the user to enter the value they want to search for
target_value = get_user_input()

# Perform sequential search
seq_found, seq_iterations = sequential_search(vector, target_value)

# Perform binary search
bin_found, bin_iterations = binary_search(vector, target_value)

# Inform the user about the results
print(f"Vector: {vector}")
print(f"Sequential Search - Found: {seq_found}, Iterations: {seq_iterations}")
print(f"Binary Search - Found: {bin_found}, Iterations: {bin_iterations}")
