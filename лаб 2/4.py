# 4. Даны два трёхзначных числа. 
# Найти общую сумму, разность, произведение их цифр, 
# а также частное от деления суммы цифр первого числа на сумму цифр второго числа. 

a = 123
b = 234
def destruct(num):
    d1, d2, d3 = 0, 0, 0
    d1 = num % 10
    num //= 10
    d2 = num % 10
    num //= 10
    d3 = num % 10
    return [d3, d2, d1]
a_d = destruct(a)
b_d = destruct(b)
a_sum = sum(a_d)
b_sum = sum(b_d)
a_diff = a_d[0] - a_d[1] - a_d[2]
b_diff = b_d[0] - b_d[1] - b_d[2]
a_mult = a_d[0] * a_d[1] * a_d[2]
b_mult = b_d[0] * b_d[1] * b_d[2]

ab_div = a_sum/b_sum