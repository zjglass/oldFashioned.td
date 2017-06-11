import kivy

from kivy.app import App
from kivy.uix.label import Label

class oldFashionedTDApp(App):
	def build(self):
		return Label(text = 'oldFashioned.td')

if __name__ == '__main__':
	oldFashionedTDApp().run()