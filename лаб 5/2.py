import json
import matplotlib.pyplot as plt

with open('лаб 5/2.json', 'r', encoding="utf-8") as j: 
    json_data = json.load(j) 

name = "Иванов Иван Иванович 0"
year = 2010
x = []
y = []
for i in json_data["workers"]:
    if i["ФИО"] == name:
        for j in i["Выплаты"]:
            if int(j["Год"]) == year:
                x.append(j["Месяц"])
                y.append(int(j["Размер выплаты"]))

plt.bar(x, y, width=0.4, color = 'green')
plt.xlabel('месяц')
plt.ylabel('выплата')
plt.legend()
plt.show()

x = []
y = []
payment = []
payment_max = []
payment_min = []
year = 2011
for i in json_data["workers"]:
    worker_payment = 0
    worker_month_count = 0
    for j in i["Выплаты"]:
        if int(j["Год"]) == year:
            worker_payment += int(j["Размер выплаты"])
            worker_month_count += 1
            payment.append(int(j["Размер выплаты"]))
    payment_max.append(max(payment))
    payment_min.append(min(payment))
    x.append(worker_payment//worker_month_count)
    y.append(i["ФИО"])

plt.pie(x, labels= y)
plt.show()

plt.bar(y, payment_max, 0.4, color = 'red')
plt.bar(y, x, 0.4, color = 'green')
plt.bar(y, payment_min, 0.4, color = 'blue')
plt.show()