from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.toolbar import MDTopAppBar
import random
import os

KV = '''
MDScreen:
	AnchorLayout:
		anchor_x: 'center'
		anchor_y: 'top'
		MDTopAppBar:
			title: "Images Roller"
    Image:
        id: dice_state
        size_hint: (0.4, 0.4)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        source: "assets/1.jpg"
	MDRaisedButton:
		id: 'roll_button'
		text: "ROLL"
		pos_hint: {'center_x':0.5, 'center_y':0.3}
		on_release: app.play()
'''

class MainApp(MDApp):
	def __init__(self):
		super().__init__()
		self.kvs = Builder.load_string(KV) 

	def build(self):
		screen = Screen()
		screen.add_widget(self.kvs)
		return screen
		
	def play(self):
		subfolder_name = "assets"
		current_directory = os.getcwd()
		subfolder_path = os.path.join(current_directory, subfolder_name)
		file_list = os.listdir(subfolder_path)
		file_list = [f for f in file_list if os.path.isfile(os.path.join(subfolder_path, f))]
		file_list = (["1.JPG","2.JPG","3.JPG","4.JPG","5.JPG","6.JPG","7.JPG","8.JPG","9.JPG","10.JPG","11.JPG"])
		dice_face = random.choice(file_list)
		file_name = "assets/" + dice_face
		self.kvs.ids.dice_state.source = file_name


MainApp().run()