import os, sys
import subprocess
from dark_libs.Functions import *
class PIP():
	def __init__(self):
		self.module = _.args[0]
		self.Send_Message = _.Send_Message
		self.Main()

	def Main(self):
		try:
			subprocess.check_call([os.path.dirname(os.path.abspath(sys.argv[0])) + "\\" + "python.exe","-c","import " + line])
			self.Send_Message.Send("%E2%9C%94%EF%B8%8F Found (" + module + ")" + " Module")
		except:
			self.Send_Message.Send("%F0%9F%93%8C Installing (" + module + ")" + " Module...")
			install = Install_Module(module)
			if install == True:
				self.Send_Message.Send("%E2%9C%94%EF%B8%8F Installed (" + module + ")" + " Module.")
			else:
				self.Send_Message.Send("%E2%9C%96%EF%B8%8F Failed Install (" + module + ")" + " Module.\n\n%E2%9D%96 Error : " + install)
