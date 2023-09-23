import pathlib
import time
import os
import pyuac

OBSIDIAN_DIR = pathlib.Path(r"C:\Users\Mourn\Documents\obsidian vault\100 Days Of Code")
home = pathlib.Path("C:/Users/Mourn/100_days_of_code")
invalid_input = True

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Relaunching as admin.")
        pyuac.runAsAdmin()

    print(f"New directory will be created in {home}.")

    while invalid_input:
        new_dir = input("Enter the name of the new directory to create: ")
        new_path = pathlib.Path(home, new_dir)
        try:
            os.mkdir(new_path)
        except FileExistsError as e:
                print(e)
                print("You did not enter a valid directory name.")
        else:
            invalid_input = False
    print(f"Created new directory {new_path}")
    print(f"\n{'*'*80}\n")
    f_name = input("Enter the name of the file you wish to create (include extension): ")
    print(f"{f_name} will be added to {new_path} and a symlink pointing to it in {OBSIDIAN_DIR}.")
    first_line = input("Enter the first line of the new file: ")
    original_file = pathlib.Path(new_path, f_name)
    with open(original_file, "w") as file:
        file.write(first_line)
    symlink = pathlib.Path(OBSIDIAN_DIR, f_name)
    os.symlink(src=original_file, dst=symlink)
    print(f"{f_name} has been created in {new_path} and {OBSIDIAN_DIR} with the first line of {first_line}")
    print("window will close in 3 seconds.")
    print("***END***")
    time.sleep(3)
