class Car:
    def __init__(self, make, model, year, license_plate):
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate

    def __str__(self):
        return f"{self.year} {self.make} {self.model} (License Plate: {self.license_plate})"


class Node:
    def __init__(self, car):
        self.car = car
        self.next = None


class CarQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, car):
        new_node = Node(car)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.car

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.car

    def display(self):
        current = self.front
        while current:
            print(current.car)
            current = current.next


# Example usage:
if __name__ == "__main__":
    queue = CarQueue()

    car1 = Car("Toyota", "Camry", 2020, "ABC123")
    car2 = Car("Honda", "Accord", 2019, "XYZ789")
    car3 = Car("Ford", "Mustang", 2021, "LMN456")

    queue.enqueue(car1)
    queue.enqueue(car2)
    queue.enqueue(car3)

    print("Cars in the queue:")
    queue.display()

    print("\nDequeue a car:")
    dequeued_car = queue.dequeue()
    print(dequeued_car)

    print("\nCars in the queue after dequeue:")
    queue.display()

    queue.dequeue()

    queue.display()
