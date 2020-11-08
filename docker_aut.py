import os 

os.system("tput setaf 2")  
print("\t\tThis menu is all about the Docker...")
os.system("tput setaf 1")
print("\t---------------------------------------------------")

os.system("tput setaf 3")
print(""" 
Enter 1 : To start the docker service
Enter 2 : To check the status of the docker service
Enter 3 : To know how many Images you have
Enter 4 : To Download the Image you want
Enter 5 : To Create the OS of any Image
Enter 6 : To Know how many Running OS  
Enter 7 : To Know the List of OS you have
Enter 8 : To Start the Already Installed OS (Stopped/Run)
Enter 9 : If you want the stop any os 
Enter 10 : To Exit from this menu..!! 
""")
while True :
	os.system("tput setaf 7")
	ch = input("Enter Your Choice : \n")
	
	if int(ch) == 1:
		os.system("systemctl start docker")
		os.system("systemctl enable docker")	
		
	elif int(ch) == 2:
		os.system("tput setaf 2")
		print("Type Ctrl + c to exit from here..")
		os.system("systemctl status docker")
		
		
	
	elif int(ch) == 3:
		os.system("tput setaf 6")
		os.system("docker images")

	elif int(ch) == 4:
		os.system("tput setaf 2")
		img = input("Enter Your image name which you want : \n")
		print(img)
		os.system("docker pull {}".format(img))

	elif int(ch) == 5:
		os.system("tput setaf 6")
		name = input("Enter the name for os : \n ")
		img = input("Enter Your image name for installation : \n")
		version = input("Enter the Version of image : \n")
		os.system("docker run -it --name {} {}:{}".format(name,img,version))
		os.system("tput setaf 3")

	elif int(ch) == 6:
		os.system("tput setaf 2")
		os.system("docker ps")

	elif int(ch) == 7:
		os.system("tput setaf 5")
		os.system("docker ps -a ")

	elif int(ch) == 8:
		os.system("tput setaf 2")
		name = input("Enter the name of os which you want to start :\n")
		os.system("docker start {}".format(name))
		os.system("docker attach {}".format(name))
		os.system("tput setaf 6")

	elif int(ch) == 9:
		os.system("tput setaf 6")
		name = input("Enter the name of os which you want to stop.. ")
		os.system("docker stop {}".format(name))

	elif int(ch) == 10:
		os.system("tput setaf 2")
		print("Thank You..!!")
		os.system("tput setaf 7")
		exit()
	
	else :
		os.system("tput setaf 1")
		print("Option Not Supported")

	os.system("tput setaf 1")	
	print("---------------------------------------------------------------------------------------")
	os.system("tput setaf 7")





	
