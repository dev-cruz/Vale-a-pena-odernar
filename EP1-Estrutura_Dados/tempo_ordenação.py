import timeit

'''Tempo de Ordenação do Inserção'''
insertion_setup = "from random import sample"

insertion_code = '''
def insertion(v):
    for j in range(1, len(v)):
        x = v[j]
        i = j - 1
        while i >= 0 and v[i] > x:
            v[i + 1] = v[i]
            i = i - 1
        v[i + 1] = x
    return v
    
v = sample(range(5000), 10)
v = insertion(v)
'''

insertion = timeit.timeit(setup=insertion_setup, stmt=insertion_code, number=30)
print(f'{insertion:.6f}')
####################################################################

'''Tempo de Ordenação do seleção'''

selection_setup = "from random import sample"

selection_code = '''
def seleção(v):
    r = []
    while v:
        m = min(v)
        r.append(m)
        v.remove(m)
    return r
    
v = sample(range(5000), 10)
v = seleção(v)
'''
selection = timeit.timeit(setup=selection_setup, stmt=selection_code, number=30)
print(f'{selection:.6f}')
####################################################################

'''Tempo de Ordenação do Mergesort'''

margesort_setup = "from random import sample"

margesort_code = '''
def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)


def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r
    
v = sample(range(5000), 10)
v = mergesort(v)
'''
margesort = timeit.timeit(setup=margesort_setup, stmt=margesort_code, number=30)
print(f'{margesort:.6f}')
#########################################################################

'''Tempo de Ordenação de Quicksort'''

quicksort_setup = "from random import sample"

quicksort_code = '''
def quicksort(v):
    if len(v) <= 1: return v

    pivô = v[0]
    iguais = [x for x in v if x == pivô]
    menores = [x for x in v if x < pivô]
    maiores = [x for x in v if x > pivô]
    return quicksort(menores) + iguais + quicksort(maiores)

v = sample(range(5000), 10)
v = quicksort(v)
'''
quicksort = timeit.timeit(setup=quicksort_setup, stmt=quicksort_code, number=30)
print(f'{quicksort:.6f}')

###################################################
arq = open('Ep1-Douglas_JoãoCruz.txt', 'w')
arq.write(" ------------------------EP1 ------------------------\n")
arq.write(" Aluno: Douglas Henrique Teixeira Barboza\n"
          "\tJoão Victor Cruz\n")
arq.write('''Tempo de Ordenação:\n
\t    n : 5000\n
Inserção:   {:.5f}
Seleção:    {:.5f}
Mergesort:  {:.5f}
Quicksort:  {:.5f}
'''.format(insertion, selection, margesort, quicksort))
arq.close()
