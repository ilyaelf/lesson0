team_1num = 6
team_2num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

print('"В команде Мастера кода участников: %d"' %(team_1num))
print('"Итого сегодня в командах участников: %d и %d"'%(team_1num,team_2num))
print('"Комаеда Волшебники данных решила задач:{}!"'.format(score2))
print('"Волшебники данных решили задачи за {}с."'.format(team2_time))
print(f'"Команды решили {score1} и {score2} задач"')
print(f'"Результат битвы:{challenge_result}"')
print(f'"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунд на задачу!"')