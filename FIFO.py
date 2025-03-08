
def fifo_algorithm(pages, memo_len):
    # Lista memory przechowuje widmową pamięć o rozmiarze zależnym od nas
    memory = []
    x = 0
    hit_number = 0
    # Hit Page występuje gdy dana strona znajduje się już w pamięci.
    hit = "Hit Page!"
    fault_number = 0
    # Page Fault występuje gdy danej strony nie ma w pamięci.
    fault = "Page Fault!"
    for number in pages:
        if number not in memory:
            if len(memory) > memo_len - 1:
                memory[x] = number
                x += 1
            else:
                memory.append(number)
                x += 1
            fault_number += 1
            print(f"{memory} {fault}")
            # print(f"{memory} {fault} Hit number: {hit_number}")
            if x > memo_len - 1:
                x = 0
        else:
            hit_number +=1
            print(f"{memory} {hit}")
            # print(f"{memory} {hit} Hit number: {hit_number}")
    print(f"Hit page number: {hit_number}")
    print(f"Page fault number: {fault_number}")
    return memory



