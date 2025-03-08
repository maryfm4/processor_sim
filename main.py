from FCFS import FCFS
from FIFO import fifo_algorithm
from LRU import LRU
from SJF import SJF
from page import page_generator
from process import generate_processes
from page import pages_anomaly


def menu():
    try:
        print("\nWhat algorithms you want to launch?")
        print('1. FCFS and SJF')
        print('2. FIFO and LRU')
        print('3. Beladys Anomaly test')
        print('4. End')
        x = int(input('(1-4):'))
        if x == 1:
            p_number = int(input("Enter the number of processes to generate:"))
            random_processes = generate_processes(p_number)
            print("Algorithm FCFS")
            FCFS(random_processes)
            print("Algorithm SJF")
            SJF(random_processes)
        elif x == 2:
            print("Algorithm FIFO")
            number = int(input("Enter the number of pages to generate:"))
            pages = page_generator(number, 9)
            print(pages)
            memo_len = int(input("Enter memory capacity: "))
            fifo_algorithm(pages, memo_len)
            print("Algorithm LRU")
            lru = LRU(memo_len)
            lru.add(pages)
            memo_len = int(input("Enter memory capacity: "))
            print("Algorithm FIFO")
            fifo_algorithm(pages, memo_len)
            print("Algorithm LRU")
            lru = LRU(memo_len)
            lru.add(pages)
        elif x == 3:
            print("Algorithm FIFO for memory capacity 3")
            pages = pages_anomaly
            print(pages)
            memo_len = 3
            fifo_algorithm(pages, memo_len)
            print("Algorithm LRU for memory capacity 3")
            lru = LRU(memo_len)
            lru.add(pages)

            print("Algorithm FIFO for memory capacity 4")
            pages = pages_anomaly
            print(pages)
            memo_len = 4
            fifo_algorithm(pages, memo_len)
            print("Algorithm LRU for memory capacity 3")
            lru = LRU(memo_len)
            lru.add(pages)

        elif x == 4:
            exit()

        else:
            print("Wrong input")
            menu()
    except KeyboardInterrupt:
        print("\nProgram interrupted...")


while True:
    menu()
