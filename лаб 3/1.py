import xml.etree.ElementTree as ET


tree = ET.parse('лаб 3/1.xml')
root = tree.getroot()

students_info = {}

for enrolle in root.findall("enrolle"):
        students_info[enrolle.findtext('name')] = [int(enrolle.findtext('math')), 
                                                    int(enrolle.findtext('russian')), 
                                                    int(enrolle.findtext('informatics'))]


every_over_50 = []
over_250 = [] 

for student in students_info.keys():
        scores = students_info[student]
        if sum(scores) > 250: over_250.append(student)
        if scores[0] > 50 and scores[1] > 50 and scores[2] > 50:
                every_over_50.append(student)
        print(student, 'avg score =', sum(scores)/len(scores))
        print(student, 'min score =', min(scores))
        print(student, 'max score =', max(scores))
        print()

print('over 250 enrolles:', over_250)
print('over 50 enrolles:', every_over_50)