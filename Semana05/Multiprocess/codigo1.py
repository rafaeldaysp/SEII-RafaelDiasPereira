import time
import multiprocessing


def delay(sec):
    print('Contando...')
    time.sleep(sec)
    print('Foi {} segundo(s)'.format(sec))

def multriprocess_on():

    t1 = time.perf_counter()

    processes = [multiprocessing.Process(target=delay, args=[i]) for i in range(10)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    t2 = time.perf_counter()
    print(f'Essa aplicação levou {round(t2-t1, 2)} segundos.')

if __name__ == '__main__':
    multriprocess_on()



