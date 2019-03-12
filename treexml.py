import xml.etree.ElementTree as ET  
tree = ET.parse('dataset1.xml') 
element=[] 
value=[]
root = tree.getroot()
print('hello root')
print(root.tag)
print(root.attrib)
for child in root:
	print(child.tag)
	print(child)
	for atr in child:
		#print(atr.tag)
		element.append(atr.tag)
		nid=atr.text
		value.append(nid)
		print(atr.tag + '=' + nid)
	break
print(element)
print(value)
	

