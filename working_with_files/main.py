from os import system
home = "C:\\Users\\Mourn\\100_days_of_code"
print(f"The current directory is {home}")
change = input("Do you wish to change it? y/n: ")
make_sure = 0
if change == 'y':
    #this doesnt work
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
    new_dir =input("Enter the name of the new directory to create: ")
path = f"{home}\\{new_dir}"
os.mkdir(path)
print(f"Created new directory {path}")
cd = os.chdir(path)
print(f"The current directory is {path}")
f_name = input("Enter the name of the file you wish to create (include extension): ")
file = open(f_name, "w")
first_line = input("Enter the first line of the new file: ")
file.write(first_line)
print(f"{f_name} has been created in {cd} with the first line of {first_line}")
file.close()