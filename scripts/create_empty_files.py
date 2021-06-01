# Script for create empty files for test another script
import os


def main():
    path = input("Enter absolute path: ")
    number = int(input("Number of files: "))
    ext = input("Extension file(.txt, .json, .csv): ")
    p = os.path.abspath(path)

    try:
        for n in range(number):
            file = os.path.join(p, str(n) + ext)
            open(file, 'a').close()
    except OSError:
        print('Failed creating the file')
    else:
        print('File created')


if __name__ == '__main__':
    main()
