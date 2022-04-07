import os, sys
class Restart():
	def __init__(self,_):
		self.Main()

	def Main(self):
		filename = os.path.dirname(os.path.abspath(sys.argv[0])) + "\\Main.vbs"
		os.system("taskkill /IM python.exe /F & " + filename)
