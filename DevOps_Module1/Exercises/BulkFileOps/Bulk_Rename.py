import shutil, os
from datetime import datetime


# prompt user for path
def get_Path():

    path = input('Please enter a folder:')
    print('Warning: all files in {} will be renamed'.format(path))

    # check if path exists
    if os.path.exists(path) == True:
        return path
    else:
        print ('Path does not exist, please try again...')
        get_Path()


if __name__ == '__main__':

    path = get_Path()

    # get today's date and time
    now = datetime.now()
    todayDate = now.strftime("%d_%b_%Y_(%H_%M_%S)")
    

    # get all files in the folder
    fileList = os.listdir(path)

    for file in fileList:

        # prefix name with date / time
        # set source and dest filenames
        newName = todayDate + file
        fullPathSource = path + "\\" + file
        fullPathDest = path + "\\" + newName

        # rename all files so that they are prefixed with the current date / time
        newFile = shutil.move(fullPathSource, fullPathDest)

        # print out a list of the new filenames
        print(newFile)



    

   

    

    
    