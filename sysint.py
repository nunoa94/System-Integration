#!/usr/bin/env python


from cmd import Cmd
import os, pwd, time, getpass, pass_file, grp, ipconfig_file

class SystemInt(Cmd):
	answer = "0"
	def do_pw(self, args):
		print("This is your current directory:")
		pass_file.Dir()
		print("Choose from the following: pw|date|ud|ifc|whereami|exit")

	def do_ifc(self, args):
		if (args == ""):
			print("This is the information for eth0")
		else:
			print"This is the information for",args
		ipconfig_file.eth(args)
		print("Choose from the following: pw|date|ud|ifc|whereami|exit")
	
	def do_date(self, args):
		print("Today's date and time is as follows")
		print(time.strftime("%Y%m%d%H%M%S"))
		print("Choose from the following: pw|date|ud|ifc|whereami|exit")

	def do_exit(self, args):
		print("You sure you want to exit? y/n")
		answer = raw_input()
		if (answer == "y"):
                	print("Exiting custom shell...")
                	time.sleep(2.5)
               		os._exit(1)
		if (answer == "n"):			
			sys1 = SystemInt()
			sys1.prompt = '-->'
			print("Choose from the following: pw|date|ud|ifc|whereami|exit")

	def do_ud(self, args):
		print("Displaying all user information")
		usr = getpass.getuser()
		print "User: ",usr
		usrID = pwd.getpwnam(usr).pw_uid
		print "User ID: ",str(usrID)
		groupID = pwd.getpwnam(usr).pw_gid
		print "Group ID: ",str(groupID)
		groupName = grp.getgrgid(groupID).gr_name
		print "Group Name: ",groupName
		homeDir = os.getenv("HOME")
		homeDirInfo = os.stat(homeDir)
		iNode = homeDirInfo.st_ino
		print "iNode: ",str(iNode)
		print("Choose from the following: pw|date|ud|ifc|whereami|exit")
		
	def do_whereami(self, args):
		print("***************************************")
		print("You are in a custom shell by Nuno Abibo")
		print("***************************************")
		print("Choose from the following: pw|date|ud|ifc|whereami|exit")

		

sys1 = SystemInt()
sys1.prompt = '-> '
sys1.cmdloop("Choose from the following: pw|date|ud|ifc|whereami|exit")