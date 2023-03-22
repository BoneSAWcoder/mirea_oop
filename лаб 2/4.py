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
summ = sum(a_d) + sum(b_d)
diff = sum(a_d) - sum(b_d)
a_mult = a_d[0] * a_d[1] * a_d[2]
b_mult = b_d[0] * b_d[1] * b_d[2]
mult = a_mult * b_mult
ab_div = sum(a_d)/sum(b_d)

print('сумма: ', summ)
print('разность', diff)
print('умножение', mult)
print('деление', ab_div)