from test import Apartment
from test import Tower
from test import Condominium

# 1) Construa a classe Torre e a classe Apartamento. A classe Torre deve possuir os atributos id,
# nome e endereço. A classe Apartamento deve conter os atributos, id, número do apartamento,
# número da vaga de garagem e torre.

# 2) Este condomínio, não possui vagas de garagem para todos os apartamentos.
# Isso faz com que exista uma fila de espera por vagas. Implemente uma fila de espera que contenha
# os métodos para adicionar apartamentos na fila, retirar apartamentos informando o número da vaga
# que este apartamento receberá e um método para imprimir a fila de espera.

# 3) O condomínio tem apenas 10 vagas de garagem. Então, no monento que o décimo primeiro apartamento
# for cadastrado, este apartamento deve ir para a fila de espera. Os apartamento que tem vaga de garagem,
# devem ficar na lista encadeada de apartamento com vaga, ordenados pelo número da vaga.

# 4) Construa um menu que permita ao usuário escolher as opções de:
# a) Cadastrar apartamento -> Quando o apartamento for cadastrado, se tiver vaga de garagem disponível,
#   ele deve ir para a lista encadeada, ordenada pelo número da vaga. Se não tiver mais vagas,
#   o apartamento deve ir para a fila de apartamentos que estão esperando a vaga.

# b) Liberar vaga -> O Usuário deve informar o número da vaga que será liberada,
#   então o apartamento que estiver nessa vaga deve ser colocado no fim da fila e
#   o apartamento que estiver no início da fila deve ir para a lista encadeada,
#   assumindo a vaga de garagem que foi liberada.

# c) Imprimir a lista de apartamentos que tem vaga.

# d) Imprimir a fila de apartamentos que estão esperando por vaga de garagem.


# Main function for user interaction menu
def main_menu(condominium):
    while True:
        print("\nChoose an option:")
        print("a) Register apartment")
        print("b) Release parking")
        print("c) Print list of apartments with parking")
        print("d) Print waiting queue for parking")
        print("e) Exit")

        option = input("Option: ").lower()

        if option == "a":
            apartment_id = input("Enter apartment ID: ")
            apartment_number = input("Enter apartment number: ")
            while True:
                try:
                    parking_number = int(input("Enter parking number: "))
                    break
                except ValueError:
                    print("Error: Parking number should be an integer.")

            tower_id = input("Enter tower ID: ")
            tower_name = input("Enter tower name: ")
            tower_address = input("Enter tower address: ")
            tower = Tower(tower_id, tower_name, tower_address)
            apartment = Apartment(apartment_id, apartment_number, parking_number, tower)
            condominium.register_apartment(apartment)
            # redirect to list WITH spot OR wwaiting list

        elif option == "b":
            while True:
                try:
                    parking_number = int(
                        input("Enter the parking number to be released: ")
                    )
                    break
                except ValueError:
                    print("Error: Parking number should be an integer.")
            condominium.release_parking(parking_number)
        # need to add parking spot to apartment in the queue, move apartment that released to back of queue
        elif option == "c":
            condominium.print_apartments_with_parking()

        elif option == "d":
            condominium.print_waiting_queue()

        elif option == "e":
            print("Exiting the program...")
            break

        else:
            print("Invalid option. Please choose one of the listed options.")


# Example usage of the condominium
if __name__ == "__main__":
    condominium = Condominium()
    main_menu(condominium)
