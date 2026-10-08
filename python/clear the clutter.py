#to organiza random file names to correct in clutter folder
import os
ext=".png"
l=os.listdir("clutter/")
for j in range(len(l)):
    if (l[j]).endswith(ext):
        p=l[j]
        z=f"{j+1}{ext}"
        if(p!=z): #to remove similar names
            if z not in l: #to not rename to existing names in directory
                os.rename(f"clutter/{p}",f"clutter/{z}")