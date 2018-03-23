# -*- coding: utf-8 -*- 
# {"keys": ["ctrl+shift+]"], "command": "phones", "args": { "file_path": "T:\\" }},

import xlrd
import glob
import time
import fnmatch
import os.path 
import sublime
import sublime_plugin

class PhonesCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		self.view.set_syntax_file("Packages/ActionScript/ActionScript.tmLanguage")
		lst = []
		lst_m = []
		files = []
		files_m = []

		fn_mask = u"*mail*ао*приоб*.xls"
		fn_path = args.get("file_path")
		for fname in glob.glob(fn_path + fn_mask):
			files_m.append(str(os.path.getmtime(fname)) + "|" + fname)
		files_m.sort(reverse=True)
		fname = files_m[0].split("|")[1]
		print(fname)
		rb = xlrd.open_workbook(fname, encoding_override = "utf-8")
		sheet1 = rb.sheet_by_index(0)
		for rownum in range(sheet1.nrows):
			row = sheet1.row_values(rownum)
			s1 = row[2]
			s2 = row[3].ljust(25)
			s = s1 + "|" + s2
			if row[3].replace(" ","") != "":
				lst_m.append(s)
		region = self.view.lines(sublime.Region(0, self.view.size()))[0]
		search_str = self.view.substr(region)
		lst.append(search_str)
		lst.append('---------------------------------------- --- -------------------- -------------------------')

		fn_mask = u"*спис*тел*риобье*.xls"
		fn_path = args.get("file_path")
		for fname in glob.glob(fn_path + fn_mask):
			files.append(str(os.path.getmtime(fname)) + "|" + fname)
		files.sort(reverse=True)
		fname = files[0].split("|")[1]
		print(fname)
		rb = xlrd.open_workbook(fname, encoding_override = "utf-8")
		sheet3 = rb.sheet_by_index(2)

		for rownum in range(sheet3.nrows):
			row = sheet3.row_values(rownum)
			s1 = row[0].ljust(40)
			s2 = str(row[1]).replace(".0","").ljust(3)
			s3 = row[2].ljust(20)
			sm2 = "".ljust(25)
			for sm in lst_m:
				sm1 = sm.split("|")[0].strip().lower()
				if s1.strip().lower() == sm1 and s1.strip().lower() != "":
					sm2 = sm.split("|")[1]
			s = s1 + " " + s2 + " " + s3 + " " + sm2
			if str(s2 + s3 + sm2).replace(" ","") != "":
				lst.append(s)

		for rownum in range(sheet3.nrows):
			row = sheet3.row_values(rownum)
			s4 = row[4].ljust(40)
			s5 = str(row[5]).replace(".0","").ljust(3)
			s6 = row[6].ljust(20)
			sm2 = "".ljust(25)
			for sm in lst_m:
				sm1 = sm.split("|")[0].strip().lower()
				if s4.strip().lower() == sm1 and s4.strip().lower() != "":
					sm2 = sm.split("|")[1]
			s = s4 + " " + s5 + " " + s6 + " " + sm2
			if str(s5 + s6 + sm2).replace(" ","") != "":
				lst.append(s)

		self.view.erase(edit, sublime.Region(0, self.view.size()))
		for i,s in enumerate(lst):
			if i < 2:
				self.view.insert(edit, self.view.size() , s + '\n')
			if i > 1 and s.lower().find(search_str.lower()) > -1:
				self.view.insert(edit, self.view.size() , s + '\n')
		self.view.sel().clear()
		self.view.sel().add(region)
