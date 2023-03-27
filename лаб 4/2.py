import json
import datetime as dt

with open('лаб 4/2.json', 'r', encoding="utf-8") as j: 
    json_data = json.load(j) 

cost_input = int(input('cost_input = '))
apartments_costs_above = []

district_input = (input('district_input = '))
apartments_square_costs_in_district = []

apartments_in_task_2_3 = []

last_year_adds = []
for i in json_data["apartments"]:
    if int(i["cost"]) > cost_input:
        apartments_costs_above.append(i["address"])
    
    if i["district"] == district_input:
        apartments_square_costs_in_district.append(int(i["cost"])/float(i["square"]))

    if int(i["floor"]) == 2 and float(i['square']) > 40:
        apartments_in_task_2_3.append(i["address"])
    
    i_date = dt.datetime.strptime(i["DateOfPlacement"], "%d.%m.%Y")
    if i_date.year == dt.datetime.now().year - 1:
        last_year_adds.append(i["address"])
    

print(apartments_costs_above)
try: 
    print(sum(apartments_square_costs_in_district) / len(apartments_square_costs_in_district))
except: ...
print(apartments_in_task_2_3)

print(dt.datetime.now() - i_date)