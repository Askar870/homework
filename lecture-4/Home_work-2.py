import random as r


# функция сортировки пузырьком
def bubble(x):
    for i in range(kol - 1):
        for j in range(kol - i - 1):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]


# проверка
def prov(x):
    try:
        s = int(x)
    except:
        print("Введите число")
        exit()


# ввод колличества чисел + проверка
kol = input("Количество чисел = ")
prov(kol)

kol = int(kol)

max_n = input("Максимальное число = ")
prov(max_n)

max_n = int(max_n)

a = [r.randint(0, max_n) for _ in range(kol)]

print(a)

# сортировка списка [a] и последующий вывод
bubble(a)
print(a)
