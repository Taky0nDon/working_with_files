<<<<<<< HEAD
import pathlib
home = pathlib.Path("C:/Users/Mourn/100_days_of_code")
# os.chdir(home)
# pwd = os.getcwd()
print(f"The current directory is {home}")
change = input("Do you wish to change it? y/n: ")
make_sure = 0
if change == 'y':
    # this doesn't work
    # scan = input("Do you want to scan for a new directory? y/n: ")
    # if scan == 'y':
    #     path1 = "C:/"
    #     system('dir {path1}')
    #     next = input("Choose another fold to scan? y/n: ")
    #     if next == 'y':
    #         next_dir = input("Enter the directory to scan")
    #         system('dir {path+"next_dir"}')

    while make_sure != 'y':
        new_dir = input("Enter the correct path: ")
        print(f"You entered {new_dir}")
        make_sure = input("Is this correct? y/n")
else:
    try:
        new_dir = input("Enter the name of the new directory to create: ")
        new_path = pathlib.Path(f"{home}/{new_dir}")
        new_path.mkdir()
    except FileExistsError:
        not_valid = True
        while not_valid:
            print("You did not enter a valid directory name.")
            new_dir = input("Enter the name of the new directory to create: ")
            # new_path = f"{home}/{new_dir}"
            home.mkdir(new_dir)
            not_valid = False
print(f"Created new directory {new_path}")
# os.chdir(path)
# pwd = os.getcwd()
print(f"The current directory is {new_path}")
f_name = input("Enter the name of the file you wish to create (include extension): ")
with open(f"{new_path}/{f_name}", "w") as file:
    first_line = input("Enter the first line of the new file: ")
    file.write(first_line)
print(f"{f_name} has been created in {new_path} with the first line of {first_line}")
=======
import pathlib
import time
import os


import pyuac


OBSIDIAN_DIR = pathlib.Path(r"C:\Users\Mourn\Documents\obsidian vault\100 Days Of Code")
HOME = pathlib.Path("C:/Users/Mourn/100_days_of_code")

def create_dir() -> bool | pathlib.Path:
    new_dir = input("Enter the name of the new directory to create: ")
    new_path = pathlib.Path(HOME, new_dir)
    try:
        os.mkdir(new_path)
    except FileExistsError as e:
        print(e)
        print("You did not enter a valid directory name.")
        return False
    else:
        return new_path 

def create_file(parent_dir) ->tuple[str, str]:
    file_name = input("Enter the name of the file you wish to create (include extension): ")
    original_file = pathlib.Path(parent_dir, file_name)
    symlink = pathlib.Path(OBSIDIAN_DIR, file_name)
    first_line = input("Enter the first line of the new file: ")
    with open(original_file, "w") as file:
        file.write(first_line)
    return file_name, first_line


def main():
    valid = False
    ending = False
    while not valid:
        valid = create_dir()
    new_path = valid
    print(f"New directory will be created in {HOME}.")

    print(f"Created new directory {new_path}")
    print(f"\n{'*'*80}\n")

    file_name, first_line = create_file(new_path)

    print(f"{file_name} will be added to {new_path} and a symlink pointing to it in {OBSIDIAN_DIR}.")

    print(f"{file_name} has been created in {new_path} and {OBSIDIAN_DIR} with the first line of {first_line}")
    print("window will close in 3 seconds.")
    print("***END***")
    while not ending:
        end = input("Operation successful. Enter 'y' to close the window")
        if end.lower() == "y":
            ending = True
            time.sleep(1)

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Relaunching as admin.")
        pyuac.runAsAdmin()
    else:
        main() 
>>>>>>> main
