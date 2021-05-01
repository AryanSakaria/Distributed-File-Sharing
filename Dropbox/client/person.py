import sys
import Pyro5.errors
from Pyro5.api import Proxy
import serpent
import os



def create_account(dropbox, username):
	# print("The user name is: ", username)
	# # print(dropbox.users.keys())
	# print("it exists: ", dropbox.check_user(username))
	if dropbox.check_user(username):
		print("User already exists")
		return False
	else:
		print("Enter password")
		passwd = input()
		dropbox.create_user(username, passwd)
		return True

def login(dropbox, username):
	# print("Enter username")
	# username = input()
	if dropbox.check_user(username):
		print("Enter passwd")
		passwd = input()
		if dropbox.check_passwd(username, passwd):
			print("Login successful")
			input("Press enter to continiue")
			os.system('clear')
			return True
		else:
			print("wrong password")
			input("Press enter to continiue")
			os.system('clear')
			return False
	else:
		print("user doesn't exist")
		input()
		os.system('clear')
		return False


def download_client(dropbox, username, filename):
	#code for local processing download
	file_content = dropbox.download_file(username, filename)
	data = serpent.tobytes(file_content)
	with open(filename, "wb") as f:
		f.write(data)

def bytes_from_file(filename, chunksize=8192):
	with open(filename, "rb") as f:
		while True:
			chunk = f.read(chunksize)
			if chunk:
				for b in chunk:
					yield b
			else:
				break


def upload_client(dropbox, username, filename):
	#code for local processing download
	with open(filename, 'rb') as f:
		file_content = f.read()

	# ser_bytes = serpent.dumps(file_content)
	# print(ser_bytes)

	dropbox.upload_file(username, filename, file_content)


	






def login_loop(dropbox, username):
	os.system('clear')
	print("Enter one of the following commands: ")
	print(" 1. list_files")
	print(" 2. list_users")
	print(" 3. list_user_files user")
	print(" 4. download file")
	print(" 5. upload file")
	print(" 6. download user file")
	print(" 7. logout\n")
	command = input().split(' ')
	# print(command.split())

	if command[0] == "list_files":
		files = dropbox.list_files(username)
		os.system('clear')
		print("The files are:")
		for i, file in enumerate(files):
			print(i, file)
		input("Press enter to continiue")
		os.system('clear')
	elif command[0] == "list_users":
		#List all users who have stored their files
		users = dropbox.list_users()
		os.system('clear')
		print("The users on server are:")
		for i, user in enumerate(users):
			print(i, user)
		input("Press enter to continiue")
		os.system('clear')

	elif command[0] == "list_user_files":
		os.system('clear')
		if dropbox.check_user(command[1]):
			files = dropbox.list_user_files(command[1])
			print("The files of user", command[1], " are: ")
			for i, file in enumerate(files):
				print(i, file)
		else:
			print("user doesn't exist")

		input("Press enter to continiue")
		os.system('clear')

	elif command[0] == 'download':
		# print("Here download praf aryan")
		# print(command)
		if len(command) == 2:
			download_client(dropbox, username, command[1])
		elif len(command) == 3:
			download_client(dropbox, command[1], command[2])
		input("Download complete. Press enter to continiue")
		os.system('clear')

	elif command[0] == 'upload':
		filename = command[1]
		upload_client(dropbox, username, filename)
		input("Upload complete. Press enter to continiue")
		os.system('clear')
		# print("uploading file: ")
		# upload_client()
	elif command[0] == 'logout':
		os.system('clear')
		print("Thank you!")
		# input("Press enter to continiue")
		return False

	return True



if __name__ == '__main__':
	loop_flag = True
	print("Welcome! Enter an option below: ")
	print("1. Create account")
	print("2. Log in")
	print("3. Exit")
	sys.excepthook = Pyro5.errors.excepthook

	dropbox = Proxy("PYRONAME:dropbox")
	# janet = Person("Janet")
	# henry = Person("Henry")
	# janet.visit(warehouse)
	# henry.visit(warehouse)

	int_input = int(input())
	if int_input == 1:
		# print("Over here")
		print("Enter username")
		username = input()
		loop_flag = create_account(dropbox, username)

	if int_input == 2:
		print("Enter username")
		username = input()
		loop_flag = login(dropbox, username)

	if int_input == 3:
		print("Thank you")
		loop_flag = False

	while (loop_flag):
		loop_flag = login_loop(dropbox, username)