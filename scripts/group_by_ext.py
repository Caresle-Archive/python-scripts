# Script for group differents files in a single folder
import os


def main():
    path = input("Path for group:")
    p = os.path.abspath(path)
    file_ext = input("Extension file (.json, .txt, .csv): ")
    folder_name = file_ext.split(".")
    folder_path = os.path.join(p, folder_name[1])
    file_transfer = 0
    for file in os.listdir(p):
        if file.endswith(file_ext):
            try:
                os.mkdir(folder_path)
            except FileExistsError:
                pass
            else:
                print("Folder create")
            try:
                file_path_old = os.path.join(p, file)
                file_path_new = os.path.join(folder_path, file)
                os.rename(file_path_old, file_path_new)
                file_transfer += 1
            except FileExistsError:
                print(f"There is a '{file}' already with the same name in the folder")

    print(f"{file_transfer} were moved")


if __name__ == '__main__':
    main()