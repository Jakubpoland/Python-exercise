import os

# Check if a file exists
if os.path.exists("myfile.txt"):
    print("myfile.txt exists")
else:
    print("myfile.txt does not exist")

# Create a new directory
os.mkdir("mydir")

# Rename a file
os.rename("oldfile.txt", "newfile.txt")

# Get the current working directory
cwd = os.getcwd()
print("Current working directory:", cwd)

# Get the login name of the current user
username = os.getlogin()
print("Current user:", username)



def current_path():
    print("Current working directory before")
    print(os.getcwd())
    print()


# Driver's code 
# Printing CWD before 
current_path()

# Changing the CWD 
os.chdir('../')

# Printing CWD after 
current_path()