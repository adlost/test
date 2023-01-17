import os
import sys

def help():
	return """
	This script was made to list unique file names.
	There are two ways to use it, with an argument in CLI and interactive mode. 
	[arg] - path to workdir, if argument not specified interactive mode will start.

	Examples:
	print_names.py [arg]
	"""

def list_files(lst):
	temp_lst = []
	for item in lst:
		if 'my_dir_' in item:
			temp_lst.extend(os.listdir(item))
	good_lst = sorted(list(set(temp_lst)))
	for i in good_lst:
		print(i)



def ask_path_way():
	PATH = input("Please specify path to my_dir_ : ")
	if PATH == "":
		print("Check current dir...")
		print(os.listdir(path="."))
		list_files(os.listdir(path="."))
	
	elif os.path.exists(PATH):
		print("Check specified dir...")
		os.chdir(PATH)
		list_files(os.listdir(path="."))

	else:
		print("Error 2. Wrong path")
		ask_path_way()

def cli_path_way(PATH):	
	if os.path.exists(PATH):
		print("Check specified dir...")
		os.chdir(PATH)
		list_files(os.listdir(path="."))
	else:
		print("Error 2. Wrong path. Please check.")



if __name__ == "__main__":
	count = len(sys.argv)
	if count == 1:
		ask_path_way()
	elif count == 2:
		if sys.argv[1] in ["-h","-help","--h","--help","h", "help"]:
			print(help())
		else:
			cli_path_way(sys.argv[1])
	else:
		print("Error 1. More then one argument used.\nTry again.")
