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
