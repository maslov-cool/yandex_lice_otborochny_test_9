lst = ['плач', 'жерло', 'лапоть', 'герольд', 'ехидна', 'цвет']
for j in lst:
    for k in lst:
        for q in lst:
            for n in lst:
                for a in lst:
                    for el in lst:
                        if len(['гроза', j, k, q, n, a, el]) == len({'гроза', j, k, q, n, a, el}) and len('гроза') != len(j) and len(j) != len(k) and len(k) != len(q) and len(q) != len(n) and len(n) != len(a) and len(a) != len(el) and len(set('гроза').intersection(j)) == 1 and len(set(j).intersection(k)) == 1 and len(set(k).intersection(q)) == 1 and len(set(q).intersection(n)) == 1 and len(set(n).intersection(a)) == 1 and len(set(a).intersection(el)) == 1:
                            print(f'гроза-{j}-{k}-{q}-{n}-{a}-{el}')
