#3. Известна денежная сумма. Разменять её купюрами 500, 100, 10 и монетой 2 руб., если это возможно.

money = 594
fives = money//500
hundreds = money%500 // 100
tens = money%100 // 10
twos = money%100%10 // 2
if str(money)[-1] in ('1', '3'):
    print('разменять невозможно')
else: 
    print(f'{fives} * 500, {hundreds} * 100, {tens} * 10, {twos} * 2')