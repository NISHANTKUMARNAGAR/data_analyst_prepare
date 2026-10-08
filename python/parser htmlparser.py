from html.parser import HTMLParser

class Myparser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print("start tag:",tag)
        for i in range(len(attrs)):
            if (attrs[i][1]):
                print("->", attrs[i][0], ">", attrs[i][1])
            else:
                print("->", attrs[i][0], ">", "None")
    def handle_endtag(self,tag):
        print("end tag:",tag)
    def handle_startendtag(self,tag,attrs):
        print("start end tag:",tag)
        for i in range(len(attrs)):
            if (attrs[i][1]):
                print("->", attrs[i][0], ">", attrs[i][1])
            else:
                print("->", attrs[i][0], ">", "None")
    def handle_data(self,data):
        #this data includes all data like data inside tags,whitespace inside tags
        #newline,Any raw text that is not part of a tag, comment, or declaration
        if(data!="\n"): #because after input "\n" is added so this
                        #it also treats that as data so we ignore that
            print(">>> Data")
            print(data)
    def handle_comment(self,data):
        if "\n" in data:
            print(">>> Multi-line Comment")
            #multi-line comment
            # because it finds "\n" in multiline comment as added
            # in after taking inout().rstrip() so i dont have to
            # write for it explicitly and add a new line
            print(data)
        else:
            print(">>> Single-line Comment")
            # as single line comment wont use more than one line so
            # it wont be able to add any "\n" inside that comment
            print(data)

p=Myparser()
p.feed("<html><head><title>test</title></head><!--[if IE 9]>IE9-specific content"
       "<![endif]-->"
       "<body><h1>h1 content</h1>"
       "<img src='testimage.jpg' height='900'/>"
       "</body></html>")

#if while taking input you strip() to remvoe any whitespace
#always add "\n" it after as strip() with nothing inside also
#remove the new line character
"""html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n' #because it contains multiline comments"""

