import json

with open('лаб 4/opop.json', 'r', encoding="utf-8") as j: 
    json_data = json.load(j) 

c = 0
for i in json_data['content']['universalCompetencyRows']:
    c += 1
for i in json_data['content']['commonCompetencyRows']:
    c += 1
print (c)

for i in json_data['content']['professionalStandards']:
    print(i['content'])

for i in json_data['content']['universalCompetencyRows']:
    print(i['competence']['code'])
    print(i['competence']['title'])
    print()

while True:
    user_input = input('введите код компетенции:')
    for i in json_data['content']['universalCompetencyRows']:
        if i['competence']['code'] == user_input:
            for j in i['indicators']:
                print(j['content'])
                break
    print('Кода не существует')