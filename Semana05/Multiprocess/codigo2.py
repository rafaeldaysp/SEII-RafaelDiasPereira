import time
import concurrent.futures


def delay(sec):
    print('Contando...')
    time.sleep(sec)
    return 'Foi {} segundo(s)'.format(sec)

def multriprocess_on():
    t1 = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(delay, [1, 2, 3, 4, 5])
    print(results)
    for result in results:
        print(result)
    t2 = time.perf_counter()
    print(f'Essa aplicação levou {round(t2-t1, 2)} segundos.')

if __name__ == '__main__':
    multriprocess_on()



