import os
def main():
    OsSelect = str(input("For Windows File system path enter 'Win' for other press 'Mac'"))
    Path = str(input('Enter Folder Name: '))
    if (OsSelect == "Win"):
        Path = Path.replace('\\',"/")
    StartingName = str(input("File Starting Name: (Note: blank if just want Counting.)"))
    EndingName = str(input("File Ending Name:(Note: blank if don't want anything.)"))
    FileType = str(input("File Type: "))
    i = 0 
    for list in os.listdir(Path):
        NewFilesName = f'{StartingName}{str(i)}{EndingName}.{FileType}'
        source = f'{Path}/{list}'
        renames = f'{Path}/{NewFilesName}'
        os.rename(source, renames)
        i += 1


if __name__ == "__main__":
    main()
# print(Path)