# third party dependencies
import numpy as np
from numpy.random import seed
from numpy.random import randint
from prettytable import PrettyTable

# native dependencies
from time import time
import random

# sort algorithms
from insertion import insertion
from merge import mergesort
from quicksort import quicksort
from selection import selection

#search algorithms
from binary_search import binary_search
from sequential_search import sequential_search

def calculate_time(unordered_array, array_len):
    for function in functions:
        start = time()
        ordered_array = function(unordered_array)
        end = time()
        total = end - start
        formated_time = round(total, 4)
        hash_table[array_len].append(formated_time)
        random_value = random.choice(ordered_array)
        total_searches = count_searches(random_value, ordered_array, formated_time)
        hash_table[array_len].append(total_searches)


def count_searches(value, ordered_array, total_time):
    start = time()
    cont = 0
    while True:
        cont += 1
        binary_search(value, ordered_array)
        sequential_search(value, ordered_array)
        end = time()
        total = end - start
        if total_time <= total:
            break
    return cont


seed(1)

functions = [insertion, selection, mergesort, quicksort]
hash_table = {
    "5000": [],
    "10000": [],
    "15000": [],
    "20000": [],
    "25000": []
}

table = PrettyTable([
    "n", "Selection", "Insertion", "Merge", "Quick",
    "Selection (buscas)", "Insertion (buscas)", "Merge (buscas)", "Quick (buscas)"
    ])

print("Aluno: Douglas Henrique Teixeira Barboza")
print("Aluno: Joao Victor da Silva Cruz")
print("FATEC - Sao Jose dos Campos")
print("Tempos de Ordenacao                              Numero de Buscas")

for i in hash_table:
    array = randint(0, 1000, int(i))
    calculate_time(list(array), i)
    row = [i] + hash_table[i]
    table.add_row(row)

print(table)