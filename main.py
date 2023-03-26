import os
home = "C:\\Users\\Mourn\\100_days_of_code"
print(f"The current directory is {home}")
new_dir =input("Enter the name of the new directory to create: ")
path = f"{home}\\{new_dir}"
os.mkdir(path)
print(f"Created new directory {path}")
cd = os.chdir(path)
print(f"The current directory is {cd}")
f_name = input("Enter the name of the file you wish to create (include extension): ")
file = open(f_name, "w")
first_line = input("Enter the first line of the new file: ")
file.write(first_line)
print(f"{f_name} has been created in {cd} with the first line of {first_line}")
file.close()