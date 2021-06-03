# Script that delete all the files with some ext
# E.g all the files with .php

import os


def main():
    path = input("Absolute path: ")
    ext = input("Extension for files to delete (.csv, .js, .php): ")
    absolute = os.path.abspath(path)
    files_erased = 0
    for file in os.listdir(absolute):
        if file.endswith(ext):
            f = os.path.join(absolute, file)
            os.remove(f)
            files_erased += 1
    print(f"files erased: {files_erased}")


if __name__ == '__main__':
    main()
