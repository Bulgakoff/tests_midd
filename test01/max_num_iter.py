num = input('>>>>>>>>>> ').split()
qwe = []
for p in num:
    qwe.append(int(p))
print(qwe)


# def recu_num(qqq):
#     if len(qqq) == 0:
#         return 0
#     elif len(qqq) == 1:
#         return qqq[0]
#     else:
#         return qqq[0] + recu_num(qqq[1:])
#
#
# res_recu_num = recu_num([625, 635])
# print(res_recu_num)
m = 0
qwer = []
for p in qwe:
    if p > m:
        m =p
qwer.append(m)
print(m)
print(qwer)
qq = []
for p in qwer:
    qq.append(str(p))
print(qq)
ww = []
for i in range(len(qq)):
    for j in range(len(qq[i])):
        ww .append(int(qq[i][j]))
print(ww)




def recu_num(qqq):
    if len(qqq) == 0:
        return 0
    elif len(qqq) == 1:
        return qqq[0]
    else:
        return qqq[0] + recu_num(qqq[1:])


res_recu_num = recu_num(ww)
print(res_recu_num)


