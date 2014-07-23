import os

def rename_files():
	file_list = os.listdir(r"./testdir")
	print(file_list)

	saved_path = os.getcwd()
	print(saved_path)
	os.chdir(r"./testdir")


	for file_name in file_list:
		print("old name=" + file_name)
		print("new name=" + file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))
	

rename_files()
	
