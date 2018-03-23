# -*- coding: utf-8 -*- 
# {"keys": ["ctrl+shift+="], "command": "calc"}

import sublime
import sublime_plugin

def format_1000(iNum):
	s = ""
	s1 = str(iNum).split(".")[0][::-1]
	s2 = str(iNum).split(".")[1]
	for i in range(0, len(s1), 3):
		s = s + s1[i:i+3] + " "
	result = s[::-1].strip() + "." + s2
	return result

class CalcCommand(sublime_plugin.TextCommand):
	def run(self, view):
		arr = []
		for region in self.view.sel():
			if not region.empty():
				arr.append(self.view.substr(region).split('\n'))
			else:
				line = self.view.line(sublime.Region(0, self.view.size()))
				arr = self.view.substr(line).split('\n')
		sum = 0
		for s1 in arr:
			s = ""
			for s2 in s1:
				s = s + s2
			d = 0 
			try:
				s = s.replace(" ","")
				if (s.find(",") > -1 and s.find(".") > -1):
					s = s.replace(",","")
				d = float(s.replace(",","."))
			except ValueError:
				print("[" + s + "] - wrong format!!!")
			sum = sum + d
		print("")
		print(format_1000(sum))