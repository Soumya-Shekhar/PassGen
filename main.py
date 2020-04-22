from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout

class grid(GridLayout):
	pass

class PasswordScreen(Screen):
	pass


class KeyScreen(Screen):
	pass

class ErrorScreen(Screen):
	pass


class ResultScreen(Screen):
	pass


class sm(ScreenManager):
	pass

class Pass_Gen(App,grid):
	def build(self):
		return
	def gen(self, key1, key2):
		try:
			self.pswd = ""
			self.l = []
			self.w = []
			self.seq = {}
			for i in range(74, 100):
				self.l.append(i)
			for j in range(ord('a'), ord('z'), 2):
				self.w.append(chr(j))
			for j in range(ord('b'), ord('z') + 1, 2):
				self.w.append(chr(j))
			self.seq = {self.l[i]: self.w[i] for i in range(len(self.l))}
			self.x = int(key1)
			self.k = str(615742 * self.x + 2347952)
			self.z = int(key2)
			self.n = []
			for num in self.k:
				self.n.append(num)
			for i in range(len(self.n)):
				self.n[i] = int(self.n[i])
				self.n[i] = self.n[i] + self.z
			for dig in self.n:
				self.pswd = self.pswd + str(self.seq.get(dig))
		except:
			self.pswd = 'Invalid Input!' + " " + "Please Input Integer only!"
		return self.pswd



if __name__ == "__main__":
	Pass_Gen().run()

