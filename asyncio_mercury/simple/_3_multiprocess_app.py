import os
import multiprocessing


def from_process():
    print(f'Дочерний процесс {os.getpid()}!')


if __name__ == '__main__':
    proc = multiprocessing.Process(target=from_process)
    proc.start()

    print(f'Текущий процесс {os.getpid()}')
    proc.join()
