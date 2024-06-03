import time
class Database:
    """
    база данных с логинами и паролями
    """
    def __init__(self):
        self.data = {}
        self.age_filter = {}
        self.title_duration = {}
        self.title_adult_mode = {}
        self.current_user = ''

    def add_user(self, username, password,age):
        self.data[username] = password
        self.age_filter[username] = int(age)

    def add_video(self,video_title):
        self.title_duration[video_title.title] = video_title.duration
        self.title_adult_mode[video_title.title] = video_title.adult_mode

    def get_video(self,search):
        search_result = []
        self.search = search.lower()
        for i in self.title_duration.keys():
            if self.search in i:
                search_result.append(i)
            else:
                continue
        return f'результат поиска:{search_result}'
    def play_video(self,video_title):
        duration = database.title_duration[video_title]
        current_position = 0
        while current_position <= duration:
            print(f'воспроизводится {video_title}  -  {current_position} секунд')
            current_position += 1
            time.sleep(1)

class User:
    """
    Класс пользователь, содерж. логин и пароль
    """
    def __init__(self, username, password, password_confirm,age):
        self.username = username
        if password == password_confirm:
            self.password = password
        self.age = age
class Video:
    video_count = 1
    def __init__(self,title,duration,adult_mode = None):
        self.title = title
        self.duration = int(duration)
        self.name = f'video{Video.video_count}'
        Video.video_count += 1

        if adult_mode == None:
            self.adult_mode = 0
        else:
            if adult_mode == False:
                self.adult_mode = 0
            else:
                self.adult_mode = 1
    def __str__(self):
        return self.name

    def add_video(self,title,duration,adult_mode):
        database.title_duration[title] = duration
        database.title_adult_mode[title] = int(adult_mode)

if __name__ == '__main__':
    database = Database()
    database.add_user('123','123','20')
    video1 = Video('Лучший язык программирования 2024 года',20 ,)
    video2 = Video('Для чего девушкам парень программист?',10,True)
    database.add_video(video1)
    database.add_video(video2)
    while True:
         choise = input(f"Приветствую!{database.current_user} Выберите действие: \n1 - Вход\n2 - Регистрация\n"
                        f"3 - Поиск видео\n4 - Воспроизвести видео\n5 - Добавить видео\n6 - Выйти\n")
         if choise == "1":
             login = input("Введите логин: ")
             password = input("Введите пароль :")
             if login in database.data:
                 if password == database.data[login]:
                     print(f'Вход выполнен,{login}')
                     database.current_user = login
                     continue
                 else:
                     print("неверный пароль")
                     continue
             else:
                 print("пользователь не найден")
                 continue
         if choise == "2":
            user = User(input("Введите логин: "), password := input("Введите пароль: "),
                        password_confirm := input("Повторите пароль: "),age := input("Введите ваш возраст: "))
            if password != password_confirm:
                print("Пароли не совпадают, попробуйте еще раз")
                continue
            if not(age.isnumeric()):
                print ("неверно введён возраст")
                continue
            database.add_user(user.username, user.password,age)
            database.current_user = user.username
            continue
         if choise == '3':
             search_request = input('введите поисковый запрос:')
             print(database.get_video(search_request))
             continue
         if choise == '4':
             if database.current_user == "":
                 print('Выполните вход или зарегистрируйтесь')
             else:
                play_video = input('введите название видео:')
                if (database.age_filter[database.current_user] < 18) and database.title_adult_mode[play_video]:
                    print('вам нет 18 для просмотра данного видео')
                    continue
                if (play_video in database.title_duration):
                    database.play_video(play_video)
                    continue
                else:
                    print('нет такого видео')
                    continue
         if choise == "5":
             new_video_title = input('введите название видео:')
             new_video_duration = input('введите продолжительность видео')
             new_video_a_m = input('видео 18+? 1 - да, 0 - нет')
             if (new_video_title not in database.title_duration):
                 Video.add_video(self=f'video{Video.video_count}',title=new_video_title,
                                 duration=int(new_video_duration),adult_mode=int(new_video_a_m))
             else:
                 continue
         if choise == '6':
             database.current_user = ""
             print('выход выполнен')
             continue
         else:
             continue