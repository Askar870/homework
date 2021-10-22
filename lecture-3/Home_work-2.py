import math as m


# функция проверки корректности ввода
def prov(x):
    dig = "0123456789"
    if (len(x) <= 0) or (x[0] not in dig) or (len(x) == 2 and x[1] not in dig):
        print("Вы должны ввести число")
        exit()
    else:
        return x


a = input("Первое число: ")
prov(a)

b = input("Второе число: ")
prov(b)

c = m.gcd(int(a), int(b))

print("НОД: ", c)
