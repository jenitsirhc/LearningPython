import concurrent.futures 
#import multiprocessing
import time


#print()
#print("Number of processors available in this device: ", multiprocessing.cpu_count())

start = time.perf_counter()
print()

def sleep_function(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return(f"Done Sleeping...{seconds}")

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(sleep_function, secs)
        
        for result in results:  
            print(result)

        #results = [executor.submit(sleep_function, sec) for sec in secs]

        #for f in concurrent.futures.as_completed(results):
        #    print(f.result())

#processes = []
#if __name__ == '__main__':
#    for _ in range(10):
#        s = multiprocessing.Process(target=sleep_function)
#        s.start()
#        processes.append(s)
#   
#    for process in processes:
#        process.join()

finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} second(s))")
