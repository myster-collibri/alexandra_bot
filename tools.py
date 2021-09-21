from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
import urllib.request
import re



def parlez(text):

    language = 'fr'

    sound = gTTS(text=text, lang=language, slow=False)
    sound.save("./voice.mp3")

    try:
        s_musicfile = "./voice.mp3"

        #s_musicfile = s_musicfile.replace(" ", "%20")

        playsound(s_musicfile)                                                         

        os.remove("./voice.mp3")
    except:
        print("error")
        os.remove("./voice.mp3")



def get_video_url(key_word):
    try:
        word=key_word.split(" ")
    except:
        word=key_word
    url="https://www.youtube.com/results?search_query={}".format(word[0])
    html=urllib.request.urlopen(url)
    videos_ids=re.findall(r"watch\?v=(\S{11})",html.read().decode())
    path_video="https://www.youtube.com/wacth?v="+videos_ids[0]

    


def recognizer_bot():
    required=-1
    for index,name in enumerate(sr.Microphone.list_microphone_names()):
        if "pulse" in name:
            required=index
    r=sr.Recognizer()
    with sr.Microphone(device_index=required) as source:
        r.adjust_for_ambient_noise(source)
        #print("Say something")
        audio=r.listen(source,phrase_time_limit=4)


    try:
        input=r.recognize_google(audio,language="fr")
        print("You said"+input)
    except:
        
        input=' '
    if len(input) > 5:
        return input
    else:
        #parlez("Je n'ai pas compris. vous dite?")
        return recognizer_bot()








#recognizer_bot()



