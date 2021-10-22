import math as m

b = int(input("Длина первой стороны = "))  # т.к. input возвращает строку, а sqrt требует численный тип данных
c = int(input("Длина второй стороны = "))
alpha = int(input("Угол между ними в градусах = "))
a = b ** 2 + c ** 2 - (2 * b * c) * m.cos(alpha)
print("Длина третьей стороны = ", m.sqrt(a))
