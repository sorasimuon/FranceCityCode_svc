import concurrent.futures
import multiprocessing
import time



def do_something(seconds):
    """
    [summary] : Simple function that print message for sleepin for n seconds

    """
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    return f'Done sleeping ...{seconds}'




if __name__ == "__main__":
    start = time.perf_counter()


    # processes = []
    # for _ in range(10):
    #     p = multiprocessing.Process(target=do_something, args=[2])
    #     p.start()
    #     processes.append(p)

    # for process in processes:
    #     process.join()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        
        # results = [executor.submit(do_something, sec) for sec in secs]
        # for f in concurrent.futures.as_completed(results):
        # print(f.result())


        results = executor.map(do_something, secs)

        for result in results:
            print(result)
    



        finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
