import xml.etree.ElementTree as ET


tree = ET.parse('лаб 3/2.xml')
root = tree.getroot()

d = {}
names = []


for student in root.findall('student'):
    names.append(student.get('name').split(' ')[0])

for i in set(names):
    d[i] = names.count(i)

for student in root.findall('student'):
    name = student.get('name')
    print(name, '; Однофамильцев:', d[name.split(' ')[0]])