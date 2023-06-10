import os

folder_path = input("Enter the folder path: ")
file_list = os.listdir(folder_path)
file_path = os.path.join(folder_path, "file_name_list.txt")

with open(file_path, "w") as file:
    for index, file_name in enumerate(file_list, 1):
        file.write(f"{index}) {file_name}\n")

print(f"{folder_path} file names listed in {file_path}")
