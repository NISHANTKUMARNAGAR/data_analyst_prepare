#importing required module convert text to speech
import win32com.client

#calling dispatch function from client module which
#interact with microsoft speech sdk to convert text to speech
speaker=win32com.client.Dispatch('SAPI.SpVoice')

#using list to print shoutout
l=['nishant','naman','seema']
for i in l:
    speaker.Speak(f"Shoutout to {i}")