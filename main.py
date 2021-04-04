import sys
import os 
import shutil

def restore ():
	print ("Restoring...")
	for i in os.listdir (os.path.join (path, "clean")):
		if i == "clean":
			continue
		shutil.move (os.path.join (path, "clean", i), path)
	os.rmdir (os.path.join (path, "clean"))

def remove ():
	print ("Removing...")
	if not os.path.exists (os.path.join (path, "clean")):
		os.mkdir (os.path.join (path, "clean"))
	for i in os.listdir (path):
		if i == "clean":
			continue
		shutil.move (os.path.join (path, i), os.path.join (path, "clean", i))


def toggle ():
	print ("Toggle")
	if not os.path.exists (os.path.join (path, "clean")):
		remove ()
	elif len (os.listdir (os.path.join (path, "clean"))) == 0:
		remove ()
	else:
		restore ()

if __name__ == "__main__":
	path = os.path.join(os.getenv ('localappdata'), "Microsoft", "Edge", "User Data", "Default", "Extensions")
	#path = r"C:\Users\Admin\Desktop\test"
	if not os.path.exists (path):
		raise Exception ("Provided path does not exist")
	args = sys.argv 
	if len (args) == 1:
		toggle ()
	elif args [1] == "add":
		restore ()
	elif args [1] == "rm":
		remove ()
	else:
		print ("Invalid command")