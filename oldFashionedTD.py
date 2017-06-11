from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class menuScreen(Screen):
	pass

class settingsScreen(Screen):
	pass

#class creditsScreen(Screen):
#	pass

#class gameScreen(Screen):
#	pass

sm = ScreenManager()
ms = menuScreen(name = 'menu')
ss = settingsScreen(name = 'credits')
sm.add_widget(ms)
sm.add_widget(ss)

class oldFashionedTDApp(App):
	def build(self):
		return sm

if __name__ == '__main__':
	oldFashionedTDApp().run()