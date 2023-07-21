import pathlib

OBSIDIAN_DIR = r"C:\Users\Mourn\Documents\100 Days of Code\Directory"
start = "C:/Users/Mourn/100_days_of_code"
home = pathlib.Path("C:/Users/Mourn/100_days_of_code")

print(f"New directory will be created in {home}.")
change = input("Create file in a different directory? y/n: ")
make_sure = "y"
if change.lower() == 'y':
    new_home = input("Please enter the correct working directory: ")
    home = pathlib.Path(new_home)

    while make_sure != 'y':
        new_dir = input("Enter the correct path: ")
        print(f"You entered {new_dir}")
        make_sure = input("Is this correct? y/n")
if make_sure == "y":
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


print(f"New file will be added to {new_path} and {OBSIDIAN_DIR}.")

directories = [OBSIDIAN_DIR, new_path]
f_name = input("Enter the name of the file you wish to create (include extension): ")
first_line = input("Enter the first line of the new file: ")

for directory in directories:
    path = directory
    with open(f"{path}/{f_name}", "w") as file:
        file.write(first_line)
print(f"{f_name} has been created in {new_path} and {OBSIDIAN_DIR} with the first line of {first_line}")
