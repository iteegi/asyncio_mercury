import threading


def from_thread():
    print(f'Поток {threading.current_thread()}!')


fth = threading.Thread(target=from_thread)
fth.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'В данный момент исполняется {total_threads} потоков')
print(f'Имя текущего потока {thread_name}')

fth.join()
