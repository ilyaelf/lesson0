import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name, mode='r') as file:
        for line in file:
            all_data.append(line)

file_list = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

start_time = time.time()
for i in range(4):
    read_info(file_list[i])
end_time = time.time()
print(f'время исполнения при линейном вызове: {end_time-start_time}сек')
'''
if __name__ == "__main__":
    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info,file_list)
    end_time = time.time()
    print(f'Время исполнения в 4 потока:{end_time-start_time}сек')
'''
