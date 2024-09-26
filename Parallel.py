import multiprocessing 
import time


#print()
#print("Number of processors available in this device: ", multiprocessing.cpu_count())

start = time.perf_counter()

def sleep_function():
    print()
    print('Sleeping 1 second...')
    time.sleep(1)
    print("Done Sleeping...")

processes = []
if __name__ == '__main__':
    for _ in range(10):
        s = multiprocessing.Process(target=sleep_function)
        s.start()
        processes.append(s)
    
    for process in processes:
        process.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s))")
