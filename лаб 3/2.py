# 2. Дан номер места в плацкартном вагоне. 
# Определить, какое это место: верхнее или нижнее, в купе или боковое. 

number = 35
a = ('сбоку', 'в купе')[number<37]
b = ('нижнее', 'верхнее')[number%2 == 0]
print(f'место {a}, {b}')
