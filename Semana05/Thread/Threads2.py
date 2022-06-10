import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print('Sleeping {} seconds'.format(seconds))
    time.sleep(seconds)
    print('Done sleeping')

threads = []
for i in range(10):
    threads.append(threading.Thread(target=do_something, args=[2]))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


finish = time.perf_counter()

print('tempo de programa = ', round(finish-start, 3))