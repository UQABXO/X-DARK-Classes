import os
class Restart():
	def __init__(self):
		self.Main()

	def Main(self):
		filename = "\\".join(os.path.abspath(__file__).split("\\")[:-2]) + "\\Main.vbs"
		os.system("taskkill /IM python.exe /F & " + filename)