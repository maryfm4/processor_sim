
class LRU:
    def __init__(self, capacity: int):
        self.pages = []
        self.memory = []
        self.capacity = capacity

    def add(self, pages):
        # Hit Page występuje gdy dana strona znajduje się już w pamięci.
        hit = "Hit Page!"
        hit_number = 0
        # Page Fault występuje gdy danej strony nie ma w pamięci.
        fault = "Page Fault!"
        fault_number = 0
        for number in pages:
            # Sprawdzam czy strona jest już w pamięci, jeśli tak to usuwam ją z obecnej pozycji przenosząc na koniec
            # listy i odświeżając jej czas użycia.
            if number in self.memory:
                self.memory.remove(number)
                self.memory.append(number)
                hit_number += 1
                print(f"{self.memory} {hit}")
                # print(f"{self.memory} {hit} Hit number: {hit_number}")
            else:
                # Sprawdzam, czy pamięć jest pełna, jeśli nie dodaje stronę do pamięci, a jeśli tak usuwam strone 'last
                # recently used'.
                if len(self.memory) < self.capacity:
                    self.memory.append(number)
                    fault_number += 1
                    print(f"{self.memory} {fault}")
                    # print(f"{self.memory} {fault} Hit number: {hit_number}")
                else:
                    self.memory.remove(self.memory[0])
                    self.memory.append(number)
                    fault_number += 1
                    print(f"{self.memory} {fault}")
                    # print(f"{self.memory} {fault} Hit number: {hit_number}")
        print(f"Hit page number: {hit_number}")
        print(f"Page fault number: {fault_number}")