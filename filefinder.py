import os
import filecmp
from tqdm import tqdm


def main():
    drive_choosed_by_user = input("Enter the drive you want to scan : ")
    drive_letter = drive_choosed_by_user.capitalize()
    start_drive = drive_letter+ ":/"
    print("Enter f for File Search, d for Directory search")
    search_type = input("Please Enter your search type: ")
    if search_type == "f":
        file_name = input("Enter the filename you want to search: ")
        file_finder(file_name,start_drive)
    elif search_type == "d":
        dir_name = input("Enter the directory name you want to search: ")
        dir_finder(dir_name,start_drive)


def file_finder(file_name,start_drive):
    for root,dirs,files in os.walk(start_drive):
        if file_name in files:
            print("File found")
            location = root+"\\"+file_name
            print(location)
            print("What do you want to do with the File ?")
            print(" Find Duplicates in current Directory : D \n Delete the file : d \n Rename the File R")
            user_operation_input = input("Please enter your operation : ")

            if user_operation_input == "D":
                findduplicate(location,start_drive)
            exit()



def dir_finder(dir_name,start_drive):
    for root,dirs,files in os.walk(start_drive):
        if dir_name in dirs:
            print("Directory Found")
            location = root+"\\"+dir_name
            print(location)
            print("What do you want to do with the Directory ?")
            dir_operation_input = input("d For Delete ,r for Rename, dt for Details " )
            if dir_operation_input == "d":
                print("Deleting the selected directory")
                os.remove(location)
                print("%s has been removed successfuly",dir_name)

            exit()


def findduplicate(location,start_drive):
    print('comparing files')
    path, dirs, files = next(os.walk(start_drive))
    file_count = len(files)
    print('file_count',file_count)
    # for root,dirs,files in os.walk(start_drive):
        
    #     for one_file in files:
    #         print(one_file)
    #         new_file_location = root+"\\"+one_file
    #         print(filecmp.cmp(location,new_file_location,shallow=False))

        



if __name__ =="__main__":
    main()