# -*- coding: utf-8 -*- 
# {"keys": ["ctrl+shift+p"], "command": "fprint"}

import os
import codecs
from _winreg import *
from subprocess import call
import sublime, sublime_plugin

class FprintCommand(sublime_plugin.TextCommand):
	def run(self, view):
		fname = os.getcwd() + r'\fprint.tmp'
		f = codecs.open(fname, 'w', 'utf-8')
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				f.write(s)
			else:
				s = self.view.substr(sublime.Region(0, self.view.size()))
				f.write(s)
		f.close()

		line = self.view.line(sublime.Region(0, self.view.size()))
		arr = self.view.substr(line).split('\n')
		arr.sort(key=len, reverse=True)
		l = len(arr[0])
		font_size = 100
		if (l > 80):
			font_size = 800/l * 10
		if (l > 160):
			font_size = 50

		try:
			keyval=r'Software\Microsoft\Notepad'
			if not os.path.exists("keyval"):
				key = CreateKey(HKEY_CURRENT_USER,keyval)
			Registrykey= OpenKey(HKEY_CURRENT_USER, r'Software\Microsoft\Notepad', 0,KEY_WRITE)
			SetValueEx(Registrykey,'iPointSize',0,REG_DWORD,font_size)
			SetValueEx(Registrykey,'lfFaceName',0,REG_SZ,'Lucida Console')
			call(['NOTEPAD', '/P',fname])
			sublime.status_message('File sent to the printer!')
			SetValueEx(Registrykey,'iPointSize',0,REG_DWORD,100)
			CloseKey(Registrykey)
		except WindowsError:
			pass


		'''
		# {"keys": ["ctrl+shift+p"], "command": "fprint" }
		# HKEY_CURRENT_USER\Software\Microsoft\Notepad
		#iPointSize 100
		#lfFaceName Lucida Console
		#&l0O	portrait
		#&l1O	landscape
		#def run(self, view, **args):
		#{"keys": ["ctrl+shift+p"], "command": "fprint", "args": { "page_orientation": "portrait" } }
		#sublime.status_message(args.get('page_orientation'))

		aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
		aKey = OpenKey(aReg, r'Software\Microsoft\Notepad')
		
		for i in range(1024):
			try:
				name, value, type = EnumValue(aKey, i)
				print name, value, type
			except WindowsError:
				pass
		'''










