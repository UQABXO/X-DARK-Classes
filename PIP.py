import os, sys
import subprocess
class PIP():
	def __init__(self, _):
		self._ = _
		self.module = _.args[0]
		self.Main()

	def Main(self):
		try:
			subprocess.check_call([os.path.dirname(os.path.abspath(sys.argv[0])) + "\\" + "python.exe","-c","import " + line])
			self._.Send_Message("%E2%9C%94%EF%B8%8F Found (" + module + ")" + " Module")
		except:
			self._.Send_Message("%F0%9F%93%8C Installing (" + module + ")" + " Module...")
			self._.Install_Module(module)
