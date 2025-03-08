import random


class Process:
    def __init__(self, name, execution=None, arrival=None):
        self.name = name
        if execution is not None:
            self.execution_time = execution
        else:
            self.execution_time = random.randint(1, 100)
            # self.execution_time = 10

        if arrival is not None:
            self.arrival_time = arrival
        else:
            self.arrival_time = random.randint(1, 100)

    # Zwracany czas wykonania procesu
    def execution(self):
        return int(self.execution_time)

    # Zwracany czas przybycia procesu
    def arrival(self):
        return int(self.arrival_time)

    # Zwracana nazwa procesu
    def get_name(self):
        return str(self.name)

    def print(self):

        print('{} {} {} '.format(self.name, (int(self.arrival_time) - 1), self.execution_time))


def generate_processes(number):
    # Generuje liste procesów.
    processes = []
    for i in range(number):
        name = f"P{i + 1}"
        process = Process(name)
        processes.append(process)
    return processes
