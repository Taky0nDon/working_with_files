import os
home = "C:/Users/Mourn/100_days_of_code"
os.chdir = home
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
        new_dir = input("Enter the correct directory: ")
        print(f"You entered {new_dir}")
        make_sure = input("Is this correct? y/n")
else:
    try:
        new_dir = input("Enter the name of the new directory to create: ")
        path = f"{home}/{new_dir}"
        os.mkdir(path)
    except FileNotFoundError:
        not_valid = True
        while not_valid:
            print("You did not enter a valid directory name.")
            new_dir = input("Enter the name of the new directory to create: ")
            path = f"{home}/{new_dir}"
            os.mkdir(path)
            not_valid = False
print(f"Created new directory {path}")
os.chdir = path
print(f"The current directory is {path}")
f_name = input("Enter the name of the file you wish to create (include extension): ")
file = open(f_name, "w")
first_line = input("Enter the first line of the new file: ")
file.write(first_line)
print(f"{f_name} has been created in {path} with the first line of {first_line}")
file.close()
