import os
import foldersList
import encrypter
if __name__ == "__main__":
    for folder in foldersList.folders:
        files = os.listdir(folder)
        for file in files:
            encrypter.encrypt(folder+"/"+file,folder,file)



