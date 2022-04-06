import os
class Restart():
	def __init__(self):
		self.__file__ = _.__file__
		self.Main()

	def Main(self):
		filename = "\\".join(os.path.abspath(_.__file__).split("\\")[:-2]) + "\\Main.vbs"
		os.system("taskkill /IM python.exe /F & " + filename)
