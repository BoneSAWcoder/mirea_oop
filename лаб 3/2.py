import xml.etree.ElementTree as ET
from prettytable import PrettyTable as pt

tree = ET.parse('лаб 3/2.xml')
root = tree.getroot()


students_in_group_1 = []
for student in root.findall("student[@group = 'ТШБО-01-22']"):
    name = student.get('name').split(' ')
    students_in_group_1.append(name[0] +' '+ name[1][0] +'. '+ name[2][0] +'.')

print('2.1')
print('Студенты в группе ТШБО-01-22:', students_in_group_1)
print()

tasks_counter = 0
tasks_done_counter = 0
subject_tasks = {}
for subject in root.findall('student[@name = "Гаврилушкин Сергей Андреевич"]/subject'):
    tasks = int(subject.findtext('tasks'))
    tasks_done = int(subject.findtext('tasks_done'))
    subject_tasks[subject.get('name')] = (tasks, tasks_done)

    tasks_counter += tasks
    tasks_done_counter += tasks_done

table = pt()
table.field_names = ['Предмет','Выполнено задач','%']

subjects_over_50 = []
for key in subject_tasks:
    if subject_tasks[key][1] / subject_tasks[key][0] > 0.5: subjects_over_50.append(key)
    table.add_row([key, 
                    subject_tasks[key][0] - subject_tasks[key][1], 
                    round(subject_tasks[key][1] / subject_tasks[key][0] * 100,2)])

print('2.2, 2.4')
print(table)
print()
print('2.3, 2.5')
print('Студент готов на', round(tasks_done_counter/tasks_counter*100, 2), '%')   
print('Студени готов более чем на 50%:', subjects_over_50)