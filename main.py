from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty,StringProperty
from kivy.lang import Builder
from kivy.core.window import Window
import threading
import os
#from alexandra_bot import alexandra
import sys
from kivy.clock import Clock
from tools import recognizer_bot

Window.maximize()
Builder.load_string('''
<MainWindow>:
	Image:
		source:'eyes1.zip'
		anim_delay:0
	BoxLayout:
		size_hint:0.5,0.1
		pos:int(root.size[0]/3),0
		TextInput:
			background_color:0,1,0,0
			foreground_color:51/255+.0,255/255+.0,51/255+.0,1
			text:app.message
			#halign:'center'


		
		
	''')

class Bot_thread(threading.Thread):

	def __init__(self,callback_fx):
		threading.Thread.__init__(self)
		self.fx=callback_fx
		self.termite_process=False
		self.sys=sys

	def run(self):

		while True:
			if self.termite_process:
				self.sys.exit()
			self.fx()

	def close(self):
		self.termite_process=True


class MainWindow(FloatLayout):

	"""Le layout principal"""
	app=App.get_running_app()


class Alexandre(App):
	main_layout=ObjectProperty()
	bot_thread=ObjectProperty()
	message=StringProperty()

	def build(self):

		#self.bot_thread=Bot_thread(alexandra)
		#self.bot_thread.start()


		self.main_layout=MainWindow()
	
		return self.main_layout

	def on_start(self):
		#Clock.schedule_interval(main,2)
		from alexandra_bot import alexandra
		self.bot_thread=Bot_thread(alexandra)
		self.bot_thread.start()

	def on_stop(self):
		self.bot_thread.close()
		os.remove("./serial.txt")
		sys.exit()



if __name__=="__main__":
	Alexandre().run()