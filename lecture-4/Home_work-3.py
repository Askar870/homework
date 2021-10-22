import random as r


# сортировка богосортом
def otsort(х):
    n = len(х)
    for i in range(0, n - 1):
        if х[i] > х[i + 1]:
            return False
    return True


def peremesh(х):
    n = len(х)
    for i in range(0, n):
        ra = r.randint(0, n - 1)
        х[i], х[ra] = х[ra], х[i]


def b_sort(х):
    n = len(х)
    while not otsort(х):
        peremesh(х)


# проверка
def prov(x):
    try:
        s = int(x)
    except:
        print("Введите число")
        exit()


# без заддержки выводятся только 8 элементов
kol = 8

max_n = input("Максимальное число = ")
prov(max_n)

max_n = int(max_n)

a = [r.randint(0, max_n) for _ in range(kol)]

print(a)
b_sort(a)
print(a)
