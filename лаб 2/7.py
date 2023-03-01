# 7. Дано трехзначное число, в котором все цифры различны. 
# Получить шесть чисел, образованных при перестановке цифр заданного числа.
a = str(123)
b = []
for i in range (3):
    for j in range(3):
        for k in range(3):
            if j == i or k == i or k == j: continue
            b.append(a[i] + a[j]+ a[k])
