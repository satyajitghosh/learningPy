import multiprocessing as mp
import os

def square_numbers():
    for i in range(1000):
        i * 1

if __name__ == '__main__':
    num_cpu = os.cpu_count()

    # Create a list of processes to be run in parallel.
    # A function is assigned to each process object

    processes = []
    for i in range(num_cpu):
        process = mp.Process(target=square_numbers)
        processes.append(process)
    
    # The processes are started
    for process in processes:
        process.start()

    # The program doesnt move further until all the processes have ended.
    for process in processes:   
        process.join()
