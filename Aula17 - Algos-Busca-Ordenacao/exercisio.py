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

def linear_search(arr, target):
    index = 0
    while index < len(arr):
        if arr[index] == target:
            print(f"Found with: {index + 1} iterations" )
            return index
        index += 1
    
    print(f"Number not found after {index +1} i")
    return -1
    
numbers = [1,2,3,4,5,6,7]
target = input("Type a number to search for: ")

linear_search(numbers, target)

def binary_search(arr, target):
    start = 0
    end = target-1
    
    while (start <= end):
        center = start + (end-start) /2
