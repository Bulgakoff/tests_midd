# Определить существование треугольника и его тип
#
# По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного
# из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

abc = input('треугольник ------------>  ').split()


def tri(qwe):
    tri_list = []
    for p in qwe:
        try:
            tri_list.append(int(p))
        except ValueError as a:
            print(f'====== {a}')
    if len(tri_list) < 3:
        print('не достаточно сторон')
    elif len(tri_list) > 3:
        print('пепребор ')
    elif len(tri_list) == 3:
        print('трьеугольниек')
        if tri_list[0] == tri_list[1] == tri_list[2]:
            print('равны стороны')
        elif tri_list[0] != tri_list[1] != tri_list[2]:
            print('разны стороны')
        else:
            print('равнобедренн')
    return tri_list


res_tri = tri(abc)
print(res_tri)
print(f'>>>>>>> {len(res_tri)}')
