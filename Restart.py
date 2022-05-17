import os, sys
class Restart():
	def __init__(self):
		self.Main()

	def Main(self):
		filename = os.path.dirname(sys.executable) + "\\Main.vbs"
		os.system("taskkill /IM python.exe /F & " + filename)
