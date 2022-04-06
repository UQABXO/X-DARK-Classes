import sys
import os
import win32com.shell.shell as shell
class Ask_Admin():
	def __init__(self):
		self.Main()

	def Main(self):
		if sys.argv[-1] != 'asadmin':
			script = os.path.abspath(sys.argv[0])
			params = ' '.join([script] + sys.argv[1:] + ['asadmin'])
			while True:
				#try:
					print(sys.executable + " " + params)
					shell.ShellExecuteEx(lpVerb='runas', lpFile="cmd.exe", lpParameters="/c " + sys.executable + " " + params)
					os.system("taskkill /IM python.exe /F")
				#except Exception as ex:
				#	pass
Ask_Admin()
