import xml.etree.ElementTree as ET
tree = ET.parse('лаб 3/test.xml')
root = tree.getroot()

for book in root.findall("Books/Book"):
        print(book) 
        title = book.find('Title').text
        author = book.find('Author').text 
        id=book.get('id') 
        #ol=book.find('Title').get('ol') 
        print(id, title, author)