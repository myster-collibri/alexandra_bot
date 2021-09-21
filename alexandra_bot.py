from kivy.app import App
import speech_recognition as sr
import pywhatkit
import os
import wikipedia as wiki
from tools import parlez,recognizer_bot,get_video_url
import datetime
from protocols import shutdown_protocol

wiki.set_lang("fr")

def alexandra():
	app=App.get_running_app()
	if not os.path.isfile("./serial.txt"):
		parlez("Démarrage d'une session d'utilisation.....")
		serial=open("./serial.txt",'w')
		parlez("Que voulez vous savoir ?")

	else:
		#parlez("J'attend votre commande...")
		pass
	command=recognizer_bot()

	#app.message=command
	if 'Alexandra' in command or 'Alexandre' in command:
		command=command.replace('Alexandra',' ')
		command=command.replace('Alexandre',' ')
		command=command.lstrip(" ")
		parlez("La commande {} est en cours de traitement.. patientez s'il vous plait.".format(command))
		if 'joue-moi' in command:
			command=command.replace('joue-moi',' ')
			command=command.lstrip(" ")
			try:
				#parlez(command)
				pywhatkit.playonyt(command)
				#parlez("commande terminé")
			except:
				parlez("la recherche n'a trouvez aucune information!")

		elif 'qui est' in command:
			command=command.replace('qui est',' ')
			command=command.lstrip(' ')
			try:
				data=wiki.summary(command,1)
				#app.message=data
				parlez(data)
				#parlez("Que voulez vous d'autre ?")
			except:
				parlez("Soyez plus precis s'il vous plait!")

		elif 'il est' in command:
			time_=datetime.datetime.now().strftime('%H:%M')
			tmp=datetime.datetime.now().strftime('%p')
			date=datetime.datetime.now().strftime('%d:%m:%y')
			if tmp == 'PM':
				temps='de l\'apres midi'
			else:
				temps='de l\'avant midi'
			parlez("Il est {}, {}. et nous sommes le {} ".format(time_,temps,date))

		elif "c'est quoi" in command:
			command=command.replace("c'est quoi",' ')
			command=command.lstrip(' ')
			try:
				data=wiki.summary(command,2)
				parlez(data)
			except:
				parlez("Soyez plus precis s'il vous plait!")

		else:
			parlez("pardon pouvez vous repeter la commande s'il vous plait ?")

		if 'protocole' in command:
			command=command.replace('protocole',' ')
			if 'koala' in command:
				shutdown_protocol()


