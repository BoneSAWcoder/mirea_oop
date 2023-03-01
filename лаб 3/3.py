money = 594
fives = money//500
hundreds = money%500 // 100
tens = money%100 // 10
twos = money%100%10 // 2
if not money%2:
    print(f'{fives} * 500, {hundreds} * 100, {tens} * 10, {twos} * 2')