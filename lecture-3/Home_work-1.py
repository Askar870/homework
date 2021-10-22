# функция проверки корректности ввода
def prov(x):
    dig = "0123456789"
    if (len(x) <= 0) or (x[0] not in dig) or (len(x) == 2 and x[1] not in dig) or (float(x) % 1 != 0):
        print("Вы должны ввести число")
        exit()
    else:
        return x


a = []
n = input("Введите число:  ")
prov(n)


for i in list(range(2, int(n) + 1)):
    k = 0
    for j in list(range(1, i + 1)):
        if i % j == 0:
            k += 1
    if k == 2:
        a.append(i)
print(a)
