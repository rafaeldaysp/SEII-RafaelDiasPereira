import time

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second')
    time.sleep(1)
    print('Done sleeping')

do_something()
do_something()

finish = time.perf_counter()

print('tempo de programa = ', round(finish-start, 3))