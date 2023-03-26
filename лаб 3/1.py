import xml.etree.ElementTree as ET


tree = ET.parse('лаб 3/1.xml')
root = tree.getroot()

students_info = {}
for enrolle in root.findall("enrolle"):
        students_info[enrolle.find('name').text] = [int(enrolle.findtext('math')), 
                                                    int(enrolle.findtext('russian')), 
                                                    int(enrolle.findtext('informatics'))]

over_50 = []
over_250 = [] 

for student in students_info.keys():
        scores = students_info[student]
        scores.sort()
        if sum(scores) > 50: over_50.append(student)
        if sum(scores) > 250: over_250.append(student)
        print(student, 'avg score =', sum(scores)/len(scores))
        print(student, 'min score =', scores[0])
        print(student, 'msx score =', scores[-1])
        print()

print('over 250 enrolles:', over_250)
print('over 50 enrolles:', over_50)