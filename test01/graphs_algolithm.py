from collections import deque

graph = {}
graph['you'] = ['alice', 'bob', 'Clear']
graph['bob'] = ['Вова', 'Жора']
graph['alice'] = ['Жора']
graph['Clear'] = ['Папа', 'Баба-Яга']
graph['Вова'] = []
graph['Жора'] = []
graph['Папа'] = []
graph['Баба-Яга'] = []

search_q = deque()
search_q += graph['you']
print(graph)


def person_is_seller(name):
    return name[-2] == 'г'


# res_person_is_seller = person_is_seller('Жора')
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()  # извлекается из очереди FIFO первый элемент (значение)
        # сохраняется в person и удаляеся из  search_queue пока не опустееет если
        # не найдется искомое и тогда return False
        if person_is_seller(person):
            print(f'{person} is seller mango! ')
            return True
        else:
            search_queue += graph[person]# если искомого  нет в элементе первой очереди
            # в search_queue добавляются уже элементы второй очереди и
            # while search_queue: продолжится до False или до НАХОЖДЕНИЯ искомого
            searched.append(person)
    return False


res_search = search('you')
print(res_search)
