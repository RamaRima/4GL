# -*- coding: utf-8 -*- 
# 
# C:\Program Files (x86)\Sublime Text 2.0.2\Data\Packages\User\Default (Windows).sublime-keymap
# 
# {"keys": ["ctrl+shift+8"], "command": "p2ftp", "args": { "ip": "192.1.2.68",
#                                                          "directory": "/qbis/wrk/user_wrk/RUSH/",
#                                                          "login": "bpd",
#                                                          "password": "" }}
# {"keys": ["ctrl+shift+9"], "command": "p2ftp", "args": { "ip": "192.1.2.69",
#                                                          "directory": "/qbis/wrk/user_wrk/RUSH/",
#                                                          "login": "bpd",
#                                                          "password": "" }}

from os.path import basename
import ctypes
import ftplib
import sublime
import sublime_plugin

MB_OK       = 0x0
MB_OKCXL    = 0x01
MB_YESNOCXL = 0x03
MB_YESNO    = 0x04
MB_HELP     = 0x4000
ICON_EXLAIM = 0x30
ICON_INFO   = 0x40
ICON_STOP   = 0x10

class P2ftpCommand(sublime_plugin.TextCommand):
	def run(self, view, **args):
		ffname = self.view.file_name()
		fname = basename(ffname)
		ip = args.get("ip")
		directory = args.get("directory")
		login = args.get("login")
		password = args.get("password")
		ftp = ftplib.FTP(ip)
		ftp.login(login, password)
		ftp.cwd(directory)
		ftp.storlines("STOR " + fname, open(ffname, 'r'))
		msg = str("Upload " + fname + " to " + ip + " complete!")
		print(msg)
		ctypes.windll.user32.MessageBoxA(None, msg, "", ICON_INFO)
