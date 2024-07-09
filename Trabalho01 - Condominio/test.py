class Node:
    def __init__(self, apartment):
        self.apartment = apartment
        self.next = None


class Tower:
    def __init__(self, tower_id, name, address):
        self.id = tower_id
        self.name = name
        self.address = address


class Apartment:
    def __init__(self, apartment_id, apartment_number, parking_number, tower):
        self.id = apartment_id
        self.apartment_number = apartment_number
        self.parking_number = parking_number
        self.tower = tower


class WaitingQueue:
    def __init__(self):
        self.queue = []

    def add_apartment(self, apartment):
        self.queue.append(apartment)

    def remove_apartment(self, parking_number):
        for i, apartment in enumerate(self.queue):
            if apartment.parking_number == parking_number:
                return self.queue.pop(i)
        return None

    def remove_first(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def print_queue(self):
        if not self.queue:
            print("Waiting queue is empty.")
        else:
            print("Apartments waiting for parking space:")
            for apartment in self.queue:
                print(
                    f"Apartment {apartment.id}, Apartment Number: {apartment.apartment_number}, Parking Number: {apartment.parking_number}"
                )


class Condominium:
    def __init__(self):
        self.available_parkings = 2
        self.head = None
        self.waiting_queue = WaitingQueue()
        self.registered_apartments = set()
        self.registered_parking_numbers = set()

    def register_apartment(self, apartment):
        if not isinstance(apartment, Apartment):
            print("Error: Invalid apartment object.")
            return

        if apartment.id in self.registered_apartments:
            print(f"Error: Apartment ID {apartment.id} is already registered.")
            return

        if apartment.parking_number in self.registered_parking_numbers:
            print(
                f"Error: Parking number {apartment.parking_number} is already registered."
            )
            return

        new_node = Node(apartment)
        if self.available_parkings > 0:
            if (
                self.head is None
                or self.head.apartment.parking_number > apartment.parking_number
            ):
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                while (
                    current.next is not None
                    and current.next.apartment.parking_number < apartment.parking_number
                ):
                    current = current.next
                new_node.next = current.next
                current.next = new_node
            self.available_parkings -= 1
            self.registered_apartments.add(apartment.id)
            self.registered_parking_numbers.add(apartment.parking_number)
            print(
                f"Apartment {apartment.id} registered successfully with parking space."
            )
        else:
            self.waiting_queue.add_apartment(apartment)
            print(
                f"Apartment {apartment.id} added to the waiting queue for parking space."
            )

    def release_parking(self, parking_number):
        if not isinstance(parking_number, int):
            print("Error: Parking number should be an integer.")
            return

        if self.head is None:
            print(f"Error: Parking space {parking_number} is not currently occupied.")
            return

        if self.head.apartment.parking_number == parking_number:
            released_apartment = self.head.apartment
            self.head = self.head.next
            self.available_parkings += 1
        else:
            current = self.head
            while (
                current.next is not None
                and current.next.apartment.parking_number != parking_number
            ):
                current = current.next
            if current.next is None:
                print(
                    f"Error: Parking space {parking_number} is not currently occupied."
                )
                return
            released_apartment = current.next.apartment
            current.next = current.next.next
            self.available_parkings += 1

        print(
            f"Parking space {parking_number} has been released. Apartment {released_apartment.id} released."
        )
        self.registered_parking_numbers.remove(parking_number)

        first_in_queue = self.waiting_queue.remove_first()
        if first_in_queue:
            first_in_queue.parking_number = parking_number
            self.register_apartment(first_in_queue)
            print(
                f"Apartment {first_in_queue.id} from waiting queue now has parking space {parking_number}."
            )
            self.waiting_queue.add_apartment(released_apartment)
        else:
            self.register_apartment(released_apartment)
            print("No apartments in the waiting queue to occupy the parking space.")

    def print_apartments_with_parking(self):
        if self.head is None:
            print("No apartments registered with parking space.")
        else:
            print("List of apartments with parking space:")
            current = self.head
            while current is not None:
                apartment = current.apartment
                print(
                    f"Apartment {apartment.id}, Apartment Number: {apartment.apartment_number}, Parking Number: {apartment.parking_number}"
                )
                current = current.next

    def print_waiting_queue(self):
        self.waiting_queue.print_queue()


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

        elif option == "c":
            condominium.print_apartments_with_parking()

        elif option == "d":
            condominium.print_waiting_queue()

        elif option == "e":
            print("Exiting the program...")
            break

        else:
            print("Invalid option. Please choose one of the listed options.")


if __name__ == "__main__":
    condominium = Condominium()
    main_menu(condominium)
