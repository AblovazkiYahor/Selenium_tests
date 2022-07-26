import os
import xml.etree.cElementTree as ET
tree = ET.parse('./library.xml')
root = tree.getroot()

books = root.findall('book')

for b in books:

    title = b.find('title').text
    price = b.find('price').text
    description = b.find('description').text
    author = b.find('author').text

    print('Title: [{}]\n'
          'Price: [{}]\n'
          'Description:[{}]\n'
          'Author:[{}]'.format(title, price, description, author))








