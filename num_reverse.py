num = 53367


def num_reevr(n):
    ns = str(n)
    ns = reversed(ns)
    qwe = None
    for p in ns:
        qwe = qwe+p
    return qwe


res_num_reevr = num_reevr(num)
print(res_num_reevr)
