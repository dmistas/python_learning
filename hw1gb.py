# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

# lst = [1, 2, 4, 5, 6, 2, 5, 2]
# names = ['ivan', 'oleg', 'sosed']
#
# for name, age in zip(lst, names):
#     print(name, age)
# print(list(zip(names, age)))
# print(dict(zip(names, age)))

name = ['Pasha', 'Igor', 'Petya', 'Masha']
salary = [100, 500, 200, 150]

name_salary = dict(zip(name, salary))
print(name_salary)
with open('salary.txt', 'w', encoding='utf-8') as f:
    for key in name_salary:
        f.write(key + ' - ' + str(name_salary[key]) + '\n')
