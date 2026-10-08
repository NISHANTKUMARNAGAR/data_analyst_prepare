   #handling a xml
"""import xml.etree.ElementTree as et
#to parse from a file
tree=et.parse("data.xml")
#to get root tag
root=tree.getroot()
print("printing root:",root)
root.set("new","20") #creates a new attribute to root having name new value 20
tree.write("data.xml")
print("printing root tag name:",root.tag)
print("printing root tag attributes:",root.attrib)
#acessing particular attribute
print("printing root tag specific attribute value:",root.attrib["new"])
print("printing root tag value:",root.text)
#to find first matching child
firstchild=root.find("a")
print("first found child 'a':",firstchild)
#to print text after element ends
print("printing text after end of this element:",firstchild.tail)
#to create and alter an attribute
firstchild.set("d","10")
#to actually alter the file in memory
tree.write("data.xml")
print("printing attributes of firstchild:",firstchild.attrib)
#to remove a attribute
del root.attrib["new"]
tree.write("data.xml")
print("printing type of firstchild:",type(firstchild))
print("printing value of firstchild:",firstchild.text)
#to find all matching child (returns list)
allfirstchild=root.findall("a")
print("printing all found 'a' in xml:",allfirstchild)
print("printing value of all in allfirstchild")
for i in allfirstchild:
    print(i.text)

#to iterate through all elements
p=root.iter()
print("value of .iter on p:",p)
print("printing index,name,value of all in p:")
for i,item in enumerate(p,start=1):
    print(i,item.tag,item.text)
#to find all matching child (returns generator)
f=root.iterfind('a')
print("printing value of iterfind on root:",f)
print("printing name,value of all in f:")
for i in f:
    print(i.tag,i.text)
#to find element but just return its text
t=root.findtext("a")
print("printing value of findtext on root:",t)
t1=root.findtext("b",default=None)
print("printing value of findtext on a element that does not exist i.e. default value:",t1)
#to loop through child(tags in root or any parent tag)
print("looping through all children/element in root:")
for child in root:
    print(child.tag,child.text)
allfirstchild=root.findall("a")
print("printing all children/element in second 'a':")
for i in range(len(allfirstchild)):
    if(i==1):
        seca=allfirstchild[i]
for k in seca:
    print(k.tag,k.text)
#creating new ele.
newelem=et.SubElement(root,"map",{"attr1":'1',"attr2":'2'},age="20")
newelem.text="india"
tree.write("data.xml")
#to remove a element
tree2=et.parse("data2.xml")
root2=tree2.getroot()
for child in root2:
    root2.remove(child)
tree2.write("data2.xml")"""

#ro parse from string
"""import xml.etree.ElementTree as et
xml_string="<root><a>10</a></root>"
root=et.fromstring(xml_string)
print("printing value of fromstring func. in elementtree",root)"""

#create element and convert and print as string
"""import xml.etree.ElementTree as et
root=et.Element("student")
root.set("id","101")
#print(et.tostring(root).decode())
new_xml = et.tostring(root, encoding='unicode')
print(new_xml)"""

#create element and convert and save to xml file
"""
import xml.etree.ElementTree as et
root=et.Element("student")
root.set("id","101")
tree=et.ElementTree(root)
tree.write("output.xml",encoding="utf-8",xml_declaration=True)
"""