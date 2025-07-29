# import index
# import calendar

# index.show()

# calendar.month
# print(calendar.month(2025,3))

def speak(str):
    import win32com.client
    speaker=win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(str)

speak("hii sir")