import webbrowser
import os 
os.system("tput setaf 1")
print("\t\t!!✌  This menu is all about the webserver ✌ !!")
os.system("tput setaf 3")
print("\t--------------------------------------------------------------")
os.system("tput setaf 6")

print("""
Press 1 : To install the web server software(httpd)
Press 2 : To start the web server 
Press 3 : To check the status of the web server
Press 4 : To know the list of Files you have in webserver folder
Press 5 : To make a html file and edit it 
Press 6 : To edit any html file which is already created
Press 7 : To launch this file on web server
Press 8 : To Exit from this menu
""")
os.system("tput setaf 1")
print("---------------------------------------------------------------------------------")

while True:
	os.system("tput setaf 3")
	chac = input("Enter Your Choice Here👇 :\n")

	if int(chac) == 1:
		os.system("tput setaf 5")
		os.system("yum install httpd")
		
	elif int(chac) == 2:
		os.system("tput setaf 6")		
		os.system("systemctl start httpd")
		os.system("systemctl enable httpd")
		print("Done..!!")

	elif int(chac) == 3:
		os.system("tput setaf 3")
		os.system("systemctl status httpd")
		
	elif int(chac) == 4:
		os.system("tput setaf 5")
		os.chdir("/var/www/html/")
		os.system("ls")

	elif int(chac) == 5:
		os.system("tput setaf 2")
		os.chdir("/var/www/html/")
		name = input("Enter any name to create the html file :\n")
		os.system("vim {}.html".format(name))

	elif int(chac) == 6:
		os.system("tput setaf 2")
		os.chdir("/var/www/html/")
		name = input("Enter alredy existed file which you want to edit :\n")
		os.system("vim {}.html".format(name))

	elif int(chac) == 7:
		os.system("tput setaf 4")
		os.system("ifconfig")
		ip = input("Enter your system's IP Address :\n")
		name = input("Enter the html file name :\n")
		webbrowser.open("http://{}/{}.html".format(ip,name))

	elif int(chac) == 8:
		os.system("tput setaf 6")
		print("Thank You..!!🤞")
		os.system("tput setaf 7")
		exit()
			

	else :
		os.system("tput setaf 1")
		print("""
		Option Not Found
		You Enterd a wrong Character
		""")


	








																			

