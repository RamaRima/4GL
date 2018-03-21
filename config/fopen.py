# -*- coding: utf-8 -*- 
# Default (Windows).sublime-keymap
# {"keys": ["ctrl+shift+O"], "command": "fopen", "args": ""}

import sublime
import sublime_plugin

class FopenCommand(sublime_plugin.TextCommand):
	def run(self, view):
		for region in self.view.sel():
			sublime.active_window().open_file(self.view.substr(region))

'''
# -*- coding: utf-8 -*- 
# Default (Windows).sublime-mousemap
# {"button": "button1", "count": 1, "modifiers": ["ctrl", "shift"],"press_command": "fopen"}

import sublime
import sublime_plugin

class FopenCommand(sublime_plugin.TextCommand):
	def run(self, view):
		for region in self.view.lines(sublime.Region(0, self.view.size())):
			if region.contains(self.view.sel()[0].begin()) == True:
				sublime.active_window().open_file(self.view.substr(region))
'''