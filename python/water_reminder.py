import pyttsx3
from datetime import datetime
import subprocess

engine=pyttsx3.init()
f=open('/home/nishantnagar/PyCharmMiscProject/time.txt','r')
storedtime=datetime.strptime(f.read().strip(),'%Y-%m-%d %H:%M:%S.%f')
f.close()
currenttime=datetime.now()
diff=currenttime-storedtime
if(diff.total_seconds()>=3600):
    engine.say("Drink Water")
    engine.runAndWait()
    subprocess.run(['notify-send','Drink water'])
    f=open('/home/nishantnagar/PyCharmMiscProject/time.txt','w')
    f.write(str(datetime.now()))
    f.close()