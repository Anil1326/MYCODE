import xml.etree.ElementTree as ET
tree = ET.parse('dataset1.xml')
root = tree.getroot()
print(root.tag)
print(root[0][1].text)
for country in root.findall('country'):
	print(country.tag)
	rank = country.find('rank').text
	name = country.get('name')
	print(name+rank)

for atr in root:
	print(atr.tag)
	print(atr.attrib)
	for elem in atr:
		#print(elem.tag + '=' + elem.text)
		print(elem.attrib)