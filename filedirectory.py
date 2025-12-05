import os

def fileDirectory():
        textApp = ''
        textWrite = ''
        files = []
        folderpath = 'H:\Documents\GitHub\File directory project\File-Directory-thingy'

        allentries = os.listdir(folderpath)
        
        for entry in allentries:
            fullpath = os.path.join(folderpath, entry)
            if os.path.isfile(fullpath):
                files.append(entry.lower())

        crOrOpen = input('Would you like to create a new file, or open an existing file? (enter \'create\' or \'open\'): ')
        if crOrOpen == 'create' or crOrOpen == 'Create':
             name = input("What would you like to name the new file?: ")
             try:
                  name = str(name)
             except:
                  print('invalid name input')

             if name.lower() in files:
                     print('file already exists')
             else:
                file = open(name, 'x')
                        
        elif crOrOpen == 'open' or crOrOpen == 'Open':
            which = input("Which file would you like to open?: ")
            try:
                which = str(which)
                print(files)
            except:
                (print('invalid file name'))

                if which.lower() in files:
                    what = input("What would you like to do to the file: ")
                    try:
                        what = str(what)
                    except:
                        print('invalid action type')
                    
                    if what == 'r' or what == 'read' or what == 'Read':
                        try:
                            with open(which, 'r') as file:
                                content = file.read()
                                print(content)
                        except:
                            print('error')

                    elif what == 'a' or what == 'append' or what == 'Append':
                        try:
                            with open(which, 'a') as file:
                                textApp = input("What text would you like to append to the file?: ")
                                file.write(f' {textApp}')
                                print(f'You have appended {textApp} in the file {which}')
                        except:
                            print('error')

                    elif what == 'w' or what == 'write' or what == 'Write':
                        try:
                            with open(which, 'w') as file:
                                textWrite = input("What would you like to write in the file?: ")
                                file.write(textWrite)
                                print(f'You have written {textWrite} in the file {which}')
                        except:
                            print('error')
                    else:
                        print('invalid action')
                else:
                    print('file not found')
        else:
            print('invalid input')

while True:
    fileDirectory()