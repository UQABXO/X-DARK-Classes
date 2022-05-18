import sys, os
class Change_Dir():
	def __init__(self, _):
		self._ = " ".join(_.args)
		self.Main()
	def Main(self):
		dirname = os.path.dirname(sys.executable)
		new_dir = r"C:\Users\Public\Test2"
		os.system("cmd.exe /c taskkill /IM python.exe /F & attrib -s -h " + dirname + " & move " + dirname + " " + new_dir)
