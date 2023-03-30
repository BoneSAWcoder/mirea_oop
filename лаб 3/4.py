from prettytable import PrettyTable
import xml.etree.ElementTree as ET


tree = ET.parse('лаб 3/test.xml')
root = tree.getroot()


x = PrettyTable()
x.field_names = ['ID', 'Title', 'Author']

for book in root.findall('Books/Book'):
    x.add_row([book.get('id'), book.findtext('Title'), book.findtext('Author')])
print(x)