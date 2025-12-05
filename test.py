with open('filelist.txt') as filelist:
    files = filelist.read().split('\n')
    print(files)