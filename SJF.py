from process import Process
import copy


class SJF:
    def __init__(self, process_list):
        # Lista przechowująca obiekty processów
        self.process = []
        self.process_queue = process_list
        self.create_processes(self.process_queue)
        self.queue()

    def create_processes(self, processes):
        # Sortuję procesy po obiekcie arrival_time, aby zasymulować przychodzenie procesów
        processes.sort(key=lambda process: process.arrival_time)
        for item in processes:
            self.process.append(Process(item.name, item.execution_time, item.arrival_time))
            # print([(p.name, p.arrival_time, p.execution_time) for p in self.process])

    def queue(self):
        t = 0
        # Lista, która przechowuje aktualnie wykonujące się procesy
        running = []
        # Kopia listy procesów do kolejki
        queue = self.process.copy()
        queue_burst = []
        # Kopia listy procesów nowy obiekt
        procs = copy.deepcopy(self.process)
        # Suma czasów wykonania procesów
        exec_time_sum = sum([item.execution_time for item in queue])
        waiting_time = []
        # Sortuje procesy do momentu skończenia się obu list
        while queue or running:
            for item in queue:
                # Sprawdzam czy proces przybył
                if item.arrival_time <= t:
                    # if item not in queue_burst:
                        # if item not in running:
                            # print(f"Process {item.name} arrived at time {t}")
                    #Dodaje proces, który przybył do kolejki
                    if item not in queue_burst:
                        queue_burst.append(item)
                        queue_burst.sort(key=lambda process: process.execution_time)
                        # print(f"Process {item.name} waiting at time {t}")

            for q in queue_burst:
                if len(running) < 1:
                    # Jeśli żaden proces się nie wykonuje, rozpocznie się pierwszy proces w kolejce
                    running.append(q)
                    queue.remove(q)
                    # Usuwam z kolejki oczekiwania proces, który się zaczyna
                    if q in queue_burst:
                        queue_burst.remove(q)
                    # print(f"Process {q.name} started at time {t}")

            for item in running:
                # Obliczam czas oczekiwania dla każdego procesu
                for proc in procs:
                    if item.name == proc.name and item.execution_time == proc.execution_time:
                        wt = t - item.arrival_time
                        if wt != 0:
                            wt += 1
                        waiting_time.append(wt)
                        # print(waiting_time)
                item.execution_time -= 1
                # Usuwam wykonane procesy
                if item.execution_time == 0:
                    running.remove(item)
                    # print(f"Process {item.name} completed at time {t}")
            t += 1
        for p in queue_burst:
            print([(p.name, p.arrival_time, p.execution_time)])
        print(f"Processes completed at the time {t}")
        print(f"The average process execution time is {exec_time_sum / len(self.process)}")
        if len(waiting_time) > 0:
            print(f"The average process waiting time is {sum(waiting_time) / len(waiting_time)}")
