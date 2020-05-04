from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.storage.jsonstore import JsonStore
from kivy.uix.recycleview import RecycleView

store = JsonStore('file.json')

class grid(GridLayout):
	pass

class PasswordScreen(Screen):
	pass

class KeyScreen(Screen):
	pass

class ErrorScreen(Screen):
	pass

class RV(RecycleView):
	pass

class ResultScreen(Screen):
	pass

class FileScreen(Screen):
	pass

class sm(ScreenManager):
	pass

class SaveData(Screen):
	pass

class DelData(Screen):
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
	def webfil(self,a):
		self.fw = open("webfile.txt",'w')
		self.fw.write(a + "\n")
		self.fw.close()
	def emailfil(self,a):
		self.fe = open("emailfile.txt",'w')
		self.fe.write(a + "\n")
		self.fe.close()
	def key1fil(self,a):
		self.fk1 = open("key1file.txt",'w')
		self.fk1.write(a + "\n")
		self.fk1.close()
	def key2fil(self,a):
		self.fk2 = open("key2file.txt",'w')
		self.fk2.write(a + "\n")
		self.fk2.close()
	def websav(self):
		self.sw = open("webfile.txt")
		self.br = self.sw.read()
		self.sw.close()
		return self.br
	def emailsav(self):
		self.se = open("emailfile.txt")
		self.be = self.se.read()
		self.se.close()
		return self.be
	def key1sav(self):
		self.sk1 = open("key1file.txt")
		self.bk1 = self.sk1.read()
		self.sk1.close()
		return self.bk1
	def key2sav(self):
		self.sk2 = open("key2file.txt")
		self.bk2 = self.sk2.read()
		self.sk2.close()
		return self.bk2

if __name__ == "__main__":
	Pass_Gen().run()

