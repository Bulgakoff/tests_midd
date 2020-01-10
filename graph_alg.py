from collections import deque

graph = {}
graph['Бабушка'] = ['Папа Леша', 'Вова']
graph['Папа Леша'] = ['Соня', 'Катя']
graph['Вова'] = ['Ма2а']
graph['Ма2а'] = ['Артем']
graph['Артем'] = []
graph['Соня'] = []
graph['Катя'] = []

print(graph)


def search_on_letter(key_name):
    return key_name[-2] == '2'


def search(key_name):  # принимаем какой нибудь ключ
    search_area = deque()
    search_area += graph[key_name]
    already_ready = []
    while search_area:
        person = search_area.popleft()
        if search_on_letter(person):
            print(f'{person} наш геройпоиск закончен')
            return f' все нашлося  == {True}'
        else:
            search_area += graph[person]  # тут ступил вместо списка для значений ключа 'person' применил словарь '()'
            already_ready.append(person)
    print(f'проверенные элементы {already_ready}')
    return f' нет искомого == {False}'


res_search = search('Вова')
print(res_search)
