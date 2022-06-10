import time
import multiprocessing


def delay(sec):
    print('Contando...')
    time.sleep(sec)
    print('Foi {} segundo(s)'.format(sec))

def multriprocess_on():
    t1 = time.perf_counter()

    p1 = multiprocessing.Process(target=delay, args=[1])
    p2 = multiprocessing.Process(target=delay, args=[1])

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    t2 = time.perf_counter()
    print(f'Essa aplicação levou {round(t2-t1, 2)} segundos.')

if __name__ == '__main__':
    multriprocess_on()



