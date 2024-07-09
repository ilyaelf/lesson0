from threading import Thread
import time

def write_words(word_count,file_name):
    with open(file_name,mode='w+',encoding='utf8')as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i})\n')
            time.sleep(0.1)
        print(f"завершилась запись в файл {file_name}")

f_t_start = time.time()
write_words(10,"example1.txt")
write_words(30,"example2.txt")
write_words(200,"example3.txt")
write_words(100,"example4.txt")
f_t_end = time.time()
f_time = f_t_end-f_t_start
print(f'работа функций заняла {f_time} секунд')

t_t_start = time.time()
thread_1 = Thread(target=write_words,args = (10,"example5.txt"))
thread_2 = Thread(target=write_words,args=(30,"example6.txt"))
thread_3 = Thread(target=write_words,args=(200,"example7.txt"))
thread_4 = Thread(target=write_words,args=(100,"example8.txt"))
thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
t_t_end = time.time()
t_t_time = t_t_end - t_t_start
print(f'работа потоков заняла {t_t_time} секунд')


