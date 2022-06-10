import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print('Sleeping {} seconds'.format(seconds))
    time.sleep(seconds)
    return 'Done sleeping {}s'.format(seconds)

threads = []

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)

finish = time.perf_counter()

print('tempo de programa = ', round(finish-start, 3))